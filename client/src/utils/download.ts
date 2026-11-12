import type { AxiosResponse } from 'axios';

/**
 * 文件流下载工具函数 (TypeScript 版)
 */

/**
 * 从响应头的 Content-Disposition 解析出文件名
 * @param disposition Header 字符串
 * @param defaultName 默认保底文件名
 */
export function extractFileName(disposition?: string, defaultName = 'downloaded_file'): string {
  if (!disposition) return defaultName;

  let fileName = defaultName;

  // 1. 优先匹配 RFC 5987 编码的 UTF-8 文件名: filename*=UTF-8''%e6%b5%8b%e8%af%95.txt
  const utf8Match = disposition.match(/filename\*=UTF-8''([^;]+)/i);
  if (utf8Match && utf8Match[1]) {
    try {
      return decodeURIComponent(utf8Match[1]);
    } catch (e) {
      console.warn('[Download] decode filename failed:', e);
    }
  }

  // 2. 匹配标准引号模式: filename="abc.txt" 或 filename=abc.txt
  const normalMatch = disposition.match(/filename="?([^";]+)"?/i);
  if (normalMatch && normalMatch[1]) {
    fileName = normalMatch[1];
    try {
      fileName = decodeURIComponent(fileName);
    } catch (e) {
      // 保持原样
    }
  }

  return fileName;
}

/**
 * 触发浏览器 Blob 另存为下载
 * @param data 二进制文件内容
 * @param fileName 文件名
 */
export function saveBlobFile(data: Blob | ArrayBuffer, fileName = 'download_file'): void {
  const blob = data instanceof Blob ? data : new Blob([data]);
  const blobUrl = window.URL.createObjectURL(blob);

  const downloadLink = document.createElement('a');
  downloadLink.style.display = 'none';
  downloadLink.href = blobUrl;
  downloadLink.setAttribute('download', fileName);

  document.body.appendChild(downloadLink);
  downloadLink.click();

  // 清理 DOM 与 ObjectURL 释放内存
  setTimeout(() => {
    document.body.removeChild(downloadLink);
    window.URL.revokeObjectURL(blobUrl);
  }, 200);
}

/**
 * 快捷下载响应包装器
 * @param response Axios 响应对象
 * @param fallbackName 保底文件名
 */
export function downloadFileByResponse(response: AxiosResponse<Blob | ArrayBuffer>, fallbackName?: string): void {
  const disposition = response.headers['content-disposition'];
  const fileName = extractFileName(disposition, fallbackName);
  saveBlobFile(response.data, fileName);
}

