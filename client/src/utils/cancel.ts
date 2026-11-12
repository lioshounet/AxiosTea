import type { AxiosRequestConfig, InternalAxiosRequestConfig } from 'axios';

/**
 * 请求防重复与取消管理器 (基于现代 AbortController 标准 - TypeScript 版)
 */

// 存储当前未完成请求的映射表: Map<string, AbortController>
const pendingMap = new Map<string, AbortController>();

/**
 * 根据请求配置生成唯一 Key
 * @param config Axios 请求配置
 */
export function generateRequestKey(config: AxiosRequestConfig | InternalAxiosRequestConfig): string {
  const { method, url, params, data } = config;
  return [
    (method || '').toUpperCase(),
    url || '',
    typeof params === 'object' ? JSON.stringify(params) : params,
    typeof data === 'object' ? JSON.stringify(data) : data
  ].join('&');
}

/**
 * 添加请求到等待队列中
 * @param config Axios 请求配置
 */
export function addPending(config: AxiosRequestConfig | InternalAxiosRequestConfig): void {
  // 如果调用方通过配置显式指定 cancelDuplicate: false，则不执行重复取消
  if (config.cancelDuplicate === false) return;

  const requestKey = generateRequestKey(config);

  // 如果已经存在相同的未完成请求，取消前一个
  if (pendingMap.has(requestKey)) {
    const controller = pendingMap.get(requestKey);
    controller?.abort(`[AxiosCancel] 重复请求已自动取消: ${requestKey}`);
    pendingMap.delete(requestKey);
  }

  // 为当前请求创建新的 AbortController
  const controller = new AbortController();
  // 绑定 signal
  config.signal = controller.signal;
  pendingMap.set(requestKey, controller);
}

/**
 * 请求完成或失败后，从等待队列移除
 * @param config Axios 请求配置
 */
export function removePending(config: AxiosRequestConfig | InternalAxiosRequestConfig): void {
  if (config.cancelDuplicate === false) return;
  const requestKey = generateRequestKey(config);
  if (pendingMap.has(requestKey)) {
    pendingMap.delete(requestKey);
  }
}

/**
 * 取消当前所有正在 pending 的请求 (常用于路由切换时)
 * @param reason 取消原因
 */
export function clearAllPending(reason = '[AxiosCancel] 页面切换，取消所有未完成请求'): void {
  for (const [, controller] of pendingMap.entries()) {
    controller.abort(reason);
  }
  pendingMap.clear();
}

/**
 * 获取当前等待中的请求数量
 */
export function getPendingCount(): number {
  return pendingMap.size;
}

export default {
  generateRequestKey,
  addPending,
  removePending,
  clearAllPending,
  getPendingCount
};

