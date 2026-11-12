import { request } from '@/utils/request';
import type { AxiosRequestConfig, AxiosResponse } from 'axios';
import type { UploadResult } from '@/types/api';

/**
 * 文件上传接口 (支持监听进度)
 * @param formData 包含文件的表单数据
 * @param onProgress 进度回调函数: (percent: number) => void
 * @param extraConfig
 */
export function uploadFileApi(
  formData: FormData,
  onProgress?: (percent: number, event: any) => void,
  extraConfig: AxiosRequestConfig = {}
): Promise<UploadResult> {
  return request<UploadResult>({
    url: '/api/file/upload',
    method: 'POST',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    onUploadProgress: (progressEvent) => {
      if (progressEvent.total) {
        const percent = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        if (typeof onProgress === 'function') {
          onProgress(percent, progressEvent);
        }
      }
    },
    ...extraConfig
  });
}

/**
 * 正常文件下载接口 (返回 AxiosResponse 二进制 Blob 流)
 * @param params
 */
export function downloadFileApi(params = {}): Promise<AxiosResponse<Blob>> {
  return request<AxiosResponse<Blob>>({
    url: '/api/file/download',
    method: 'GET',
    params,
    responseType: 'blob'
  });
}

/**
 * 模拟文件下载异常 (后端报错返回 JSON)
 */
export function downloadFailApi(): Promise<AxiosResponse<Blob>> {
  return request<AxiosResponse<Blob>>({
    url: '/api/file/download-fail',
    method: 'GET',
    responseType: 'blob'
  });
}

