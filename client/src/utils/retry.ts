import type { AxiosError, AxiosInstance, InternalAxiosRequestConfig } from 'axios';

/**
 * 接口请求自动重试机制 (TypeScript 版)
 */

/**
 * 判断当前错误是否允许自动重试
 * @param error Axios 错误对象
 */
export function isRetryAllowed(error: AxiosError): boolean {
  if (error.name === 'CanceledError' || error.code === 'ERR_CANCELED') {
    return false;
  }
  if (error.code === 'ECONNABORTED' || !error.response) {
    return true;
  }
  const status = error.response.status;
  return [502, 503, 504].includes(status);
}

/**
 * 执行请求重试逻辑
 * @param axiosInstance 传入的 axios 实例
 * @param error 错误对象
 */
export function handleRequestRetry(axiosInstance: AxiosInstance, error: AxiosError): Promise<any> {
  const config = error.config as InternalAxiosRequestConfig | undefined;

  if (!config || !config.retryCount || config.retryCount <= 0) {
    return Promise.reject(error);
  }

  if (!isRetryAllowed(error)) {
    return Promise.reject(error);
  }

  config.__retryCount = config.__retryCount || 0;

  if (config.__retryCount >= config.retryCount) {
    console.warn(`[AxiosRetry] 请求 ${config.url} 已达到最大重试次数 (${config.retryCount})，停止重试。`);
    return Promise.reject(error);
  }

  config.__retryCount += 1;
  const delay = config.retryDelay || 1000;

  console.log(`[AxiosRetry] 正在为 ${config.url} 执行第 ${config.__retryCount} 次重试，将在 ${delay}ms 后触发...`);

  return new Promise((resolve) => {
    setTimeout(() => {
      if (config.signal && config.signal.aborted) {
        delete (config as any).signal;
      }
      resolve(axiosInstance(config));
    }, delay);
  });
}

