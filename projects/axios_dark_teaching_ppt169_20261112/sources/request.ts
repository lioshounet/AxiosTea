import axios, {
  type AxiosInstance,
  type AxiosRequestConfig,
  type AxiosResponse,
  type AxiosError,
  type InternalAxiosRequestConfig
} from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';
import { getAccessToken, getRefreshToken, setTokens, clearTokens } from './token';
import { addPending, removePending } from './cancel';
import { startLoading, endLoading } from './loading';
import { handleRequestRetry } from './retry';
import type { ApiResponse } from '@/types/api';

// 日志记录函数 (供教学控制台实时观察)
function recordLog(
  type: 'info' | 'success' | 'warning' | 'error',
  title: string,
  content: string,
  payload?: any
): void {
  if (typeof window !== 'undefined' && window.__ADD_AXIOS_LOG__) {
    window.__ADD_AXIOS_LOG__({ type, title, content, payload });
  }
}

/**
 * 1. 创建 Axios 核心实例
 */
const service: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API || '',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  }
});

// ======================== 双 Token 无感刷新状态变量 ========================
let isRefreshing = false; // 是否正在刷新 Token 的标志锁
let retryQueue: Array<(token: string) => void> = []; // 等待新 Token 重新派发的请求队列

/**
 * 将因 401 挂起的请求加入重发队列
 */
function subscribeTokenRefresh(cb: (token: string) => void): void {
  retryQueue.push(cb);
}

/**
 * Token 刷新成功后，批量重新执行挂起的请求
 */
function onTokenRefreshed(newToken: string): void {
  retryQueue.forEach((cb) => cb(newToken));
  retryQueue = [];
}

/**
 * 单独用于刷新 Token 的轻量 Axios 实例
 * 重点：切勿直接用主 service 实例去调刷新接口，否则若刷新接口本身报 401 会导致无限死循环！
 */
const refreshService: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API || '',
  timeout: 8000
});

// ======================== 2. 请求拦截器 (Request Interceptor) ========================
service.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    recordLog('info', '【请求拦截器触发】', `发起请求: [${config.method?.toUpperCase()}] ${config.url}`, {
      params: config.params,
      data: config.data
    });

    // 1. 加载动画处理
    if (config.showLoading) {
      startLoading(config.loadingText);
    }

    // 2. 防重复请求检查与取消处理
    addPending(config);

    // 3. 自动注入 Authorization Bearer Token
    const token = getAccessToken();
    if (token) {
      if (typeof config.headers?.set === 'function') {
        config.headers.set('Authorization', `Bearer ${token}`);
      } else {
        (config.headers as any)['Authorization'] = `Bearer ${token}`;
      }
      recordLog('info', '【注入凭证】', '成功注入 Access Token 至 Header Authorization');
    }

    return config;
  },
  (error: AxiosError) => {
    recordLog('error', '【请求拦截器报错】', error.message, error);
    return Promise.reject(error);
  }
);

// ======================== 3. 响应拦截器 (Response Interceptor) ========================
service.interceptors.response.use(
  async (response: AxiosResponse) => {
    const { config, data } = response;

    // 1. 请求完成，从 pending 列表中移除并关闭 Loading
    removePending(config);
    if (config.showLoading) {
      endLoading();
    }

    recordLog('success', '【响应拦截器触发】', `收到响应: HTTP ${response.status} 来自 ${config.url}`, data);

    // 2. 二进制文件流 / Blob 特殊处理
    if (config.responseType === 'blob' || config.responseType === 'arraybuffer') {
      const contentType = String(response.headers['content-type'] || '');
      // 核心教学坑点：若后端导出失败返回 JSON，前端设置了 responseType: 'blob' 时会被包装为 Blob！
      if (data?.type === 'application/json' || contentType.includes('application/json')) {
        try {
          const text = await (data as Blob).text();
          const errorJson = JSON.parse(text);
          ElMessage.error(errorJson.message || '文件导出失败！');
          recordLog('error', '【Blob异常捕获】', `Blob 内嵌业务错误: ${errorJson.message}`, errorJson);
          return Promise.reject(new Error(errorJson.message || '导出失败'));
        } catch (e) {
          // 不是 JSON 则继续正常走文件下载
        }
      }

      // 正常二进制文件，返回原始 response
      return response;
    }

    // 3. 统一业务状态码判断
    if (data && typeof data.code !== 'undefined') {
      if (data.code === 200 || data.code === 0) {
        // 业务成功：直接解包返回内部真正的 data
        return data.data !== undefined ? data.data : data;
      } else {
        // 业务逻辑异常
        const errMsg = data.message || '系统业务逻辑异常';
        if (config.showErrorMessage !== false) {
          ElMessage.error(errMsg);
        }
        recordLog('warning', '【业务状态码异常】', `code: ${data.code}, message: ${errMsg}`, data);
        return Promise.reject(new Error(errMsg));
      }
    }

    return data;
  },
  async (error: AxiosError<ApiResponse>) => {
    const config = error.config as InternalAxiosRequestConfig | undefined;
    const response = error.response;

    // 清理 pending 与 loading
    if (config) {
      removePending(config);
      if (config.showLoading) {
        endLoading();
      }
    }

    // 1. 如果是用户主动取消或防重复机制取消的请求
    if (axios.isCancel(error)) {
      recordLog('warning', '【请求被主动取消】', error.message || '请求已中断取消');
      console.warn('[Axios] 请求已主动取消:', error.message);
      return Promise.reject(error);
    }

    // 2. 处理 HTTP 401 授权失败与双 Token 无感刷新机制
    if (response && response.status === 401 && config) {
      recordLog('error', '【HTTP 401 未授权】', '收到 401 响应，准备触发无感刷新流程...');
      const refreshToken = getRefreshToken();

      if (!refreshToken) {
        handleLogoutRedirect('未检测到登录凭证，请重新登录');
        return Promise.reject(error);
      }

      if (isRefreshing) {
        recordLog('info', '【无感刷新】', `已有正在进行的刷新任务，将 [${config.url}] 压入等待队列`);
        return new Promise((resolve) => {
          subscribeTokenRefresh((newToken: string) => {
            if (typeof config.headers?.set === 'function') {
              config.headers.set('Authorization', `Bearer ${newToken}`);
            } else {
              (config.headers as any)['Authorization'] = `Bearer ${newToken}`;
            }
            resolve(service(config));
          });
        });
      }

      isRefreshing = true;
      recordLog('info', '【无感刷新】', '首个 401 触发，开始调用 /api/auth/refresh 刷新凭证');

      try {
        const refreshRes = await refreshService.post<ApiResponse<{ accessToken: string; refreshToken: string }>>(
          '/api/auth/refresh',
          { refreshToken }
        );
        const resData = refreshRes.data;

        if (resData.code === 200 && resData.data?.accessToken) {
          const { accessToken: newAccessToken, refreshToken: newRefreshToken } = resData.data;
          setTokens({ accessToken: newAccessToken, refreshToken: newRefreshToken });
          recordLog('success', '【无感刷新成功】', '获取到新 Token，开始重放队列中的全部请求');

          onTokenRefreshed(newAccessToken);

          if (typeof config.headers?.set === 'function') {
            config.headers.set('Authorization', `Bearer ${newAccessToken}`);
          } else {
            (config.headers as any)['Authorization'] = `Bearer ${newAccessToken}`;
          }
          return service(config);
        } else {
          throw new Error('Refresh Token 置换新 Token 失败');
        }
      } catch (refreshErr) {
        recordLog('error', '【无感刷新失败】', 'Refresh Token 已失效，需重新登录', refreshErr);
        retryQueue = [];
        handleLogoutRedirect('登录凭证已过期失效，请重新登录！');
        return Promise.reject(refreshErr);
      } finally {
        isRefreshing = false;
      }
    }

    // 3. 自动重试机制
    if (config && config.retryCount && config.retryCount > 0) {
      try {
        return await handleRequestRetry(service, error);
      } catch (retryFinalErr: any) {
        error = retryFinalErr;
      }
    }

    // 4. 通用 HTTP 状态码错误提示
    let errorMessage = '网络请求异常，请稍后重试';
    if (response) {
      const status = response.status;
      switch (status) {
        case 400:
          errorMessage = response.data?.message || '请求参数有误 (400)';
          break;
        case 403:
          errorMessage = '抱歉，您没有权限访问该资源 (403)';
          break;
        case 404:
          errorMessage = '请求的接口地址不存在 (404)';
          break;
        case 500:
          errorMessage = '服务器内部发生错误 (500)';
          break;
        case 502:
          errorMessage = '网关异常错误 (502)';
          break;
        case 503:
          errorMessage = '服务暂时不可用，服务器超载或维护 (503)';
          break;
        case 504:
          errorMessage = '网关超时 (504)';
          break;
        default:
          errorMessage = response.data?.message || `网络连接错误 (${status})`;
      }
    } else if (error.code === 'ECONNABORTED' || error.message.includes('timeout')) {
      errorMessage = '网络请求超时，请检查网络后重试';
    } else if (error.message.includes('Network Error')) {
      errorMessage = '网络连接异常，无法连接到服务器';
    }

    if (config?.showErrorMessage !== false) {
      ElMessage.error(errorMessage);
    }
    recordLog('error', '【HTTP/网络错误】', errorMessage, error);

    return Promise.reject(error);
  }
);

/**
 * 清除 Token 并提示退出
 */
function handleLogoutRedirect(tip = '登录状态已失效'): void {
  clearTokens();
  ElMessageBox.alert(tip, '系统通知', {
    confirmButtonText: '确定',
    type: 'warning'
  }).then(() => {
    if (typeof window !== 'undefined' && window.__AUTH_LOGOUT_EVENT__) {
      window.__AUTH_LOGOUT_EVENT__();
    }
  });
}

/**
 * 封装通用泛型请求方法
 * @template T 期望返回的数据载荷类型 (已经由拦截器解包)
 */
export function request<T = any>(config: AxiosRequestConfig): Promise<T> {
  return service(config) as unknown as Promise<T>;
}

export default service;
