import { request } from '@/utils/request';
import type { AxiosRequestConfig } from 'axios';
import type { UserInfo } from '@/types/api';

/**
 * 获取受保护的用户信息 (需有效 Token)
 * @param extraConfig 额外的 Axios 配置
 */
export function getUserProfileApi(extraConfig: AxiosRequestConfig = {}): Promise<UserInfo> {
  return request<UserInfo>({
    url: '/api/user/profile',
    method: 'GET',
    ...extraConfig
  });
}

