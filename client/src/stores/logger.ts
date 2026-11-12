import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { LogItem } from '@/types/api';

/**
 * 教学专用：实时请求与拦截器事件日志 Store (TypeScript 版)
 */
export const useLoggerStore = defineStore('logger', () => {
  const logs = ref<LogItem[]>([]);

  function addLog({
    type = 'info',
    title,
    content,
    payload = null
  }: {
    type?: 'info' | 'success' | 'warning' | 'error';
    title: string;
    content: string;
    payload?: any;
  }): void {
    const logItem: LogItem = {
      id: Date.now() + Math.random().toString(36).substring(2, 7),
      time: new Date().toLocaleTimeString() + '.' + String(Date.now() % 1000).padStart(3, '0'),
      type,
      title,
      content,
      payload: payload ? JSON.parse(JSON.stringify(payload)) : null
    };
    logs.value.unshift(logItem);
    if (logs.value.length > 80) {
      logs.value.pop();
    }
  }

  function clearLogs(): void {
    logs.value = [];
  }

  return {
    logs,
    addLog,
    clearLogs
  };
});

