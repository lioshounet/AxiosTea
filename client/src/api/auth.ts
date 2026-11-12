import { request } from '@/utils/request';
import type { LoginParams, LoginResult, RefreshResult } from '@/types/api';

/**
 * 用户登录
 * @param data { username, password }
 */
export function loginApi(data: LoginParams): Promise<LoginResult> {
  return request<LoginResult>({
    url: '/api/auth/login',
    method: 'POST',
    data,
    showLoading: true,
    loadingText: '正在登录...'
  });
}

/**
 * 手动刷新 Token (主要供教学调试演示)
 * @param data { refreshToken }
 */
export function refreshTokenApi(data: { refreshToken: string }): Promise<RefreshResult> {
  return request<RefreshResult>({
    url: '/api/auth/refresh',
    method: 'POST',
    data
  });
}

