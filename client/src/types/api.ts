/**
 * 通用后端响应体包装泛型接口
 * @template T 内部携带的数据类型
 */
export interface ApiResponse<T = any> {
  code: number;
  message: string;
  data: T;
}

/** 用户登录参数 */
export interface LoginParams {
  username: string;
  password: string;
}

/** 用户信息 */
export interface UserInfo {
  id?: number;
  userId?: number;
  username: string;
  name?: string;
  role?: string;
  permissions?: string[];
  loginTime?: string;
}

/** 登录接口返回的数据结构 */
export interface LoginResult {
  accessToken: string;
  refreshToken: string;
  expiresIn: number;
  userInfo: UserInfo;
}

/** 刷新 Token 接口返回结构 */
export interface RefreshResult {
  accessToken: string;
  refreshToken: string;
  expiresIn: number;
}

/** 延迟接口返回结构 */
export interface DelayResult {
  respondedAt: string;
  duration: number;
}

/** 重试接口返回结构 */
export interface RetryResult {
  attemptCount: number;
  successTime: string;
}

/** 文件上传结果 */
export interface UploadResult {
  originalName: string;
  filename: string;
  size: number;
  mimetype: string;
  url: string;
}

/** 日志项接口 */
export interface LogItem {
  id: string;
  time: string;
  type: 'info' | 'success' | 'warning' | 'error';
  title: string;
  content: string;
  payload?: any;
}

