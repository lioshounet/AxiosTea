import { request } from '@/utils/request';
import type { AxiosRequestConfig } from 'axios';
import type { DelayResult, RetryResult } from '@/types/api';

/**
 * 延迟耗时接口 (用于演示取消请求与防重复点击)
 * @param params { delay: 3000 }
 * @param extraConfig
 */
export function getDelayApi(
  params = { delay: 3000 },
  extraConfig: AxiosRequestConfig = {}
): Promise<{ message: string; data: DelayResult }> {
  return request<{ message: string; data: DelayResult }>({
    url: '/api/test/delay',
    method: 'GET',
    params,
    ...extraConfig
  });
}

/**
 * 模拟业务逻辑异常 (HTTP 200, 但 code !== 200)
 * @param extraConfig
 */
export function getBusinessErrorApi(extraConfig: AxiosRequestConfig = {}): Promise<any> {
  return request({
    url: '/api/test/business-error',
    method: 'GET',
    ...extraConfig
  });
}

/**
 * 模拟 HTTP 状态码异常 (403, 404, 500)
 * @param status 状态码
 * @param extraConfig
 */
export function getHttpErrorApi(status = 500, extraConfig: AxiosRequestConfig = {}): Promise<any> {
  return request({
    url: '/api/test/http-error',
    method: 'GET',
    params: { status },
    ...extraConfig
  });
}

/**
 * 模拟网络重试接口 (前2次503，第3次成功)
 * @param clientId 客户端唯一测试ID
 * @param extraConfig
 */
export function getRetryApi(
  clientId: string,
  extraConfig: AxiosRequestConfig = {}
): Promise<{ message: string; data: RetryResult }> {
  return request<{ message: string; data: RetryResult }>({
    url: '/api/test/retry',
    method: 'GET',
    params: { clientId },
    retryCount: 3,
    retryDelay: 1000,
    ...extraConfig
  });
}

