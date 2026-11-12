/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue';
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

interface Window {
  __ADD_AXIOS_LOG__?: (log: {
    type: 'info' | 'success' | 'warning' | 'error';
    title: string;
    content: string;
    payload?: any;
  }) => void;
  __AUTH_LOGOUT_EVENT__?: () => void;
}

