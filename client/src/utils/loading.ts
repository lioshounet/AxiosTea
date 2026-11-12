import { ElLoading } from 'element-plus';

/**
 * 并发安全的全屏 Loading 控制器 (TypeScript 版)
 */

let loadingInstance: ReturnType<typeof ElLoading.service> | null = null;
let loadingCount = 0;

/**
 * 开启 Loading
 * @param text 加载文案
 */
export function startLoading(text = '数据加载中，请稍候...'): void {
  if (loadingCount === 0) {
    loadingInstance = ElLoading.service({
      lock: true,
      text,
      background: 'rgba(0, 0, 0, 0.45)'
    });
  }
  loadingCount++;
}

/**
 * 关闭 Loading
 */
export function endLoading(): void {
  if (loadingCount <= 0) return;
  loadingCount--;
  if (loadingCount === 0 && loadingInstance) {
    // 延迟少许关闭，防止极短网络请求下的界面快速闪烁
    setTimeout(() => {
      if (loadingCount === 0 && loadingInstance) {
        loadingInstance.close();
        loadingInstance = null;
      }
    }, 100);
  }
}

/**
 * 强制重置 Loading 状态 (如页面异常或切换)
 */
export function resetLoading(): void {
  loadingCount = 0;
  if (loadingInstance) {
    loadingInstance.close();
    loadingInstance = null;
  }
}

