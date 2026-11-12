/**
 * Token 存储与管理工具 (TypeScript 版)
 */

const ACCESS_TOKEN_KEY = 'AXIOS_DEMO_ACCESS_TOKEN';
const REFRESH_TOKEN_KEY = 'AXIOS_DEMO_REFRESH_TOKEN';

export function getAccessToken(): string {
  return localStorage.getItem(ACCESS_TOKEN_KEY) || '';
}

export function setAccessToken(token: string): void {
  if (token) {
    localStorage.setItem(ACCESS_TOKEN_KEY, token);
  } else {
    localStorage.removeItem(ACCESS_TOKEN_KEY);
  }
}

export function getRefreshToken(): string {
  return localStorage.getItem(REFRESH_TOKEN_KEY) || '';
}

export function setRefreshToken(token: string): void {
  if (token) {
    localStorage.setItem(REFRESH_TOKEN_KEY, token);
  } else {
    localStorage.removeItem(REFRESH_TOKEN_KEY);
  }
}

export function setTokens(tokens: { accessToken?: string; refreshToken?: string }): void {
  if (tokens.accessToken) setAccessToken(tokens.accessToken);
  if (tokens.refreshToken) setRefreshToken(tokens.refreshToken);
}

export function clearTokens(): void {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
}

