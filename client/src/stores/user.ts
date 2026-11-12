import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { loginApi } from '@/api/auth';
import { getUserProfileApi } from '@/api/user';
import type { AxiosRequestConfig } from 'axios';
import type { UserInfo, LoginResult } from '@/types/api';
import {
  getAccessToken,
  setTokens,
  clearTokens,
  getRefreshToken
} from '@/utils/token';

export const useUserStore = defineStore('user', () => {
  const token = ref<string>(getAccessToken());
  const refreshToken = ref<string>(getRefreshToken());
  const userInfo = ref<UserInfo | null>(null);
  const tokenExpiresIn = ref<number>(0);

  const isLoggedIn = computed(() => !!token.value);

  // 登录操作
  async function login(username: string, password: string): Promise<LoginResult> {
    const res = await loginApi({ username, password });
    token.value = res.accessToken;
    refreshToken.value = res.refreshToken;
    userInfo.value = res.userInfo;
    tokenExpiresIn.value = res.expiresIn || 15;

    setTokens({
      accessToken: res.accessToken,
      refreshToken: res.refreshToken
    });

    return res;
  }

  // 获取用户信息
  async function fetchProfile(extraConfig: AxiosRequestConfig = {}): Promise<UserInfo> {
    const res = await getUserProfileApi(extraConfig);
    userInfo.value = res;
    return res;
  }

  // 退出登录
  function logout(): void {
    token.value = '';
    refreshToken.value = '';
    userInfo.value = null;
    tokenExpiresIn.value = 0;
    clearTokens();
  }

  // 刷新状态同步
  function syncTokensFromStorage(): void {
    token.value = getAccessToken();
    refreshToken.value = getRefreshToken();
  }

  return {
    token,
    refreshToken,
    userInfo,
    tokenExpiresIn,
    isLoggedIn,
    login,
    fetchProfile,
    logout,
    syncTokensFromStorage
  };
});

