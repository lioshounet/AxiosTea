import 'axios';

/**
 * 教学知识点：Axios 类型模块扩展 (Module Augmentation)
 *
 * 为什么需要扩展 AxiosRequestConfig?
 * 在企业级封装中，我们为请求拓展了诸如 cancelDuplicate (防重复)、showLoading (全局加载)、
 * retryCount (重试次数) 等自定义配置属性。
 * 通过 TypeScript 声明合并 (Declaration Merging)，可在调用 axios / request 时获得完整的类型提示与语法补全！
 */
declare module 'axios' {
  export interface AxiosRequestConfig {
    /** 是否开启防重复请求取消机制 (默认 true，传 false 则允许并发相同请求) */
    cancelDuplicate?: boolean;
    /** 是否展示全局 Loading 动画 (默认 false) */
    showLoading?: boolean;
    /** 全局 Loading 提示文本 */
    loadingText?: string;
    /** 业务状态码或 HTTP 报错时是否自动弹出 ElMessage 错误提示 (默认 true) */
    showErrorMessage?: boolean;
    /** 请求失败时最大自动重试次数 (默认 0 不重试) */
    retryCount?: number;
    /** 请求自动重试间隔延时 (毫秒，默认 1000ms) */
    retryDelay?: number;
    /** 内部使用的当前已重试计数器 */
    __retryCount?: number;
  }
}

