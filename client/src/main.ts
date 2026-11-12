import { createApp } from 'vue';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import * as ElementPlusIconsVue from '@element-plus/icons-vue';
import App from './App.vue';
import { useLoggerStore } from './stores/logger';
import { useUserStore } from './stores/user';

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(ElementPlus);

// 注册所有 ElementPlus 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

// 绑定全局日志钩子供 request.ts 跨模块轻量级投递
const loggerStore = useLoggerStore();
const userStore = useUserStore();

window.__ADD_AXIOS_LOG__ = (log) => {
  loggerStore.addLog(log);
};

window.__AUTH_LOGOUT_EVENT__ = () => {
  userStore.logout();
};

app.mount('#app');

