<template>
  <div class="app-container">
    <!-- 顶部状态栏 -->
    <header class="app-header">
      <div class="header-brand">
        <el-icon class="brand-icon" :size="26"><Promotion /></el-icon>
        <div>
          <h1 class="brand-title">Axios 工业级深度封装教学与演练平台 (TypeScript 全量版)</h1>
          <p class="brand-subtitle">Vue 3 + TypeScript + Pinia + Element Plus + Node.js 全套联动实践</p>
        </div>
      </div>

      <div class="header-auth">
        <template v-if="userStore.isLoggedIn">
          <el-tag type="success" effect="dark" class="auth-tag">
            <el-icon><User /></el-icon> 已登录: {{ userStore.userInfo?.name || userStore.userInfo?.username || '用户' }}
          </el-tag>
          <div class="token-timer" :class="{ 'token-expired': tokenCountdown <= 0 }">
            <el-icon><Timer /></el-icon>
            <span>Token剩余: <strong>{{ tokenCountdown > 0 ? tokenCountdown + 's' : '已过期(待刷新)' }}</strong></span>
          </div>
          <el-button type="danger" size="small" plain @click="handleLogout">退出登录</el-button>
        </template>
        <template v-else>
          <el-tag type="info" effect="plain">未登录</el-tag>
          <el-button type="primary" size="small" @click="handleQuickLogin">
            一键快速登录 (admin / 123456)
          </el-button>
        </template>
      </div>
    </header>

    <!-- 主工作区：左侧测试工作台 + 右侧实时日志控制台 -->
    <main class="app-main">
      <div class="workbench">
        <el-tabs v-model="activeTab" type="border-card" class="demo-tabs">
          <!-- TAB 1: 基础请求与解包 -->
          <el-tab-pane label="1. 基础请求与统一解包" name="basic">
            <div class="tab-content">
              <el-alert
                title="教学知识点：Axios 实例与数据解包 (TypeScript 泛型推导)"
                type="info"
                :closable="false"
                show-icon
                description="原生 Axios 会将后端数据包在 response.data 中。封装层在响应拦截器统一判断 code === 200 并返回 response.data.data，配合泛型 request<T>() 让前端页面直接获得精准的 TypeScript 类型智能提示！"
              />

              <div class="action-grid">
                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">标准 GET 请求 (获取用户信息)</span>
                  </template>
                  <p class="card-desc">自动在 Header 注入 Bearer Token，并在响应拦截器中完成解包与 UserInfo 类型匹配。</p>
                  <div class="card-actions">
                    <el-button type="primary" @click="onFetchUserProfile">发起 GET 请求</el-button>
                    <el-button type="info" plain @click="onFetchUserProfileWithLoading">
                      携带全局 Loading (showLoading: true)
                    </el-button>
                  </div>
                  <div v-if="profileResult" class="result-box">
                    <pre><code>{{ JSON.stringify(profileResult, null, 2) }}</code></pre>
                  </div>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">标准 POST 请求 (登录鉴权)</span>
                  </template>
                  <p class="card-desc">提交用户名密码，获取短期 AccessToken (15s) 与长期 RefreshToken。</p>
                  <div class="card-actions">
                    <el-button type="success" @click="handleQuickLogin">调用登录接口</el-button>
                    <el-button type="warning" plain @click="onLoginError">
                      测试登录错误 (故意输错密码)
                    </el-button>
                  </div>
                </el-card>
              </div>
            </div>
          </el-tab-pane>

          <!-- TAB 2: 双 Token 无感刷新 -->
          <el-tab-pane label="2. 双 Token 无感刷新机制" name="token">
            <div class="tab-content">
              <el-alert
                title="教学核心重难点：双 Token 无感刷新与请求队列重放机制"
                type="warning"
                :closable="false"
                show-icon
                description="当 Access Token 过期时服务端返回 401。前端拦截器捕获 401 后暂停该请求，用 Refresh Token 请求新 Token；若刷新期间有多个并发请求到来，放入队列挂起；新 Token 到位后批量重放，用户全程无感知。"
              />

              <div class="token-status-banner">
                <div class="status-col">
                  <span class="label">Access Token:</span>
                  <el-tag :type="userStore.token ? 'success' : 'danger'">
                    {{ userStore.token ? '已持有 (' + (tokenCountdown > 0 ? tokenCountdown + 's 有效' : '已过期') + ')' : '未获取' }}
                  </el-tag>
                </div>
                <div class="status-col">
                  <span class="label">Refresh Token:</span>
                  <el-tag :type="userStore.refreshToken ? 'success' : 'danger'">
                    {{ userStore.refreshToken ? '长期有效 (7天)' : '未获取' }}
                  </el-tag>
                </div>
              </div>

              <div class="action-grid">
                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">场景 A：单个请求过期无感重发</span>
                  </template>
                  <p class="card-desc">
                    请先登录。等待 15 秒待 AccessToken 过期后，点击下方按钮，观察控制台：请求首先收到 401，然后自动调用 /refresh 换取新 Token 并无缝重新发起原本请求！
                  </p>
                  <el-button
                    type="primary"
                    :disabled="!userStore.isLoggedIn"
                    @click="onTestSilentRefreshSingle"
                  >
                    发起请求 (自动静默刷新)
                  </el-button>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">场景 B：并发请求队列重放防死锁</span>
                  </template>
                  <p class="card-desc">
                    Token 过期时同时触发 5 个并发请求。观察控制台：<strong>仅会调用一次</strong> /refresh 接口，其余 4 个请求被挂入队列，待刷新成功后自动依次重发！
                  </p>
                  <el-button
                    type="warning"
                    :disabled="!userStore.isLoggedIn"
                    @click="onTestConcurrentSilentRefresh"
                  >
                    同时发出 5 个受保护请求
                  </el-button>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">场景 C：RefreshToken 彻底失效</span>
                  </template>
                  <p class="card-desc">
                    当用户长时间未操作，连 Refresh Token 也失效了。此时刷新接口报 401，拦截器清空本地凭证并强制弹框引导用户重新登录。
                  </p>
                  <el-button type="danger" plain @click="onTestRefreshTokenExpired">
                    使 RefreshToken 失效并触发请求
                  </el-button>
                </el-card>
              </div>
            </div>
          </el-tab-pane>

          <!-- TAB 3: 防重复请求与取消 -->
          <el-tab-pane label="3. 防重复请求与 AbortController" name="cancel">
            <div class="tab-content">
              <el-alert
                title="教学知识点：现代 AbortController 与防重复请求机制"
                type="info"
                :closable="false"
                show-icon
                description="Axios v0.22+ 废弃了 CancelToken，推荐基于标准 Web API 的 AbortController。封装层依据 [Method + URL + Params + Data] 作为唯一 Key，自动将正在 pending 的前一个请求 cancel 掉，防止用户手抖快速狂点造成的数据错乱。"
              />

              <div class="action-grid">
                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">测试 1：快速连击防重复 (耗时3秒接口)</span>
                  </template>
                  <p class="card-desc">
                    点击下方按钮将以 60ms 间隔瞬间连发 5 次相同请求。观察右侧控制台：前 4 次请求会被自动识别为重复并由 AbortController 中断取消，仅最后 1 次能顺利完成！
                  </p>
                  <el-button type="primary" @click="onFastClickFiveTimes">
                    快速狂点 5 次相同请求
                  </el-button>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">测试 2：慢速请求与手动中断取消</span>
                  </template>
                  <p class="card-desc">
                    发起一个耗时 5000ms 的慢速查询接口，随后可随时点击【手动取消】按钮将其提前中断。
                  </p>
                  <div class="card-actions">
                    <el-button type="warning" :loading="isSlowLoading" @click="onStartSlowRequest">
                      {{ isSlowLoading ? '请求执行中(等待5秒)...' : '发起 5 秒慢速请求' }}
                    </el-button>
                    <el-button type="danger" :disabled="!isSlowLoading" @click="onCancelCurrentRequest">
                      手动中断取消此请求
                    </el-button>
                  </div>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">测试 3：允许并发配置 (cancelDuplicate: false)</span>
                  </template>
                  <p class="card-desc">
                    某些场景（如批量保存不同条目或批量加载分片）需要同时并发相同的接口。传入 <code>cancelDuplicate: false</code> 即可跳过防重复逻辑。
                  </p>
                  <el-button type="success" plain @click="onAllowConcurrentRequests">
                    并发触发 3 个相同接口 (不取消)
                  </el-button>
                </el-card>
              </div>
            </div>
          </el-tab-pane>

          <!-- TAB 4: 统一错误处理与自动重试 -->
          <el-tab-pane label="4. 错误处理与自动重试" name="error">
            <div class="tab-content">
              <el-alert
                title="教学知识点：业务状态码 vs HTTP 状态码 vs 网络超时重试"
                type="error"
                :closable="false"
                show-icon
                description="区分两套错误体系：1. 业务逻辑错误 (HTTP 200, code !== 200，如余额不足)；2. 网络/HTTP 状态码异常 (403/404/500/超时)。同时对于网络抖动或 503 故障，封装层提供了可配置的指数退避自动重试机制。"
              />

              <div class="action-grid">
                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">1. 业务状态码异常 (code: 5001)</span>
                  </template>
                  <p class="card-desc">
                    HTTP 状态码是 200，但业务 code 报错。拦截器统一 ElMessage 提示并进入 catch 分支。
                  </p>
                  <el-button type="warning" @click="onTestBusinessError">测试业务错误</el-button>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">2. HTTP 状态码异常 (403 / 404 / 500)</span>
                  </template>
                  <p class="card-desc">
                    模拟常见的 HTTP 协议错误，拦截器针对各类状态码统一映射友好的中文错误说明。
                  </p>
                  <div class="card-actions">
                    <el-button size="small" type="danger" plain @click="onTestHttpError(403)">403 权限拒绝</el-button>
                    <el-button size="small" type="danger" plain @click="onTestHttpError(404)">404 路径不存在</el-button>
                    <el-button size="small" type="danger" plain @click="onTestHttpError(500)">500 服务器错误</el-button>
                  </div>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">3. 接口失败自动重试机制 (Retry Pattern)</span>
                  </template>
                  <p class="card-desc">
                    请求配置了 <code>retryCount: 3, retryDelay: 1000</code>。服务端接口前 2 次故意返回 503 报错，第 3 次成功返回。观察控制台自动在 1 秒后重发，直到最终成功！
                  </p>
                  <el-button type="success" @click="onTestAutoRetry">触发自动重试演示</el-button>
                </el-card>
              </div>
            </div>
          </el-tab-pane>

          <!-- TAB 5: 文件上传/下载与Blob -->
          <el-tab-pane label="5. 上传/下载与 Blob 异常" name="file">
            <div class="tab-content">
              <el-alert
                title="教学重难点：二进制流下载与 responseType: 'blob' 时的异常捕获"
                type="info"
                :closable="false"
                show-icon
                description="前端通过 responseType: 'blob' 接收文件。当后端导出发生错误返回 JSON 时，Axios 仍会将其打包为 Blob，若直接下载会导致下载损坏的空文件！封装层通过 res.data.text() 智能侦测 JSON 并解析出真实报错！"
              />

              <div class="action-grid">
                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">文件上传与实时进度监听 (onUploadProgress)</span>
                  </template>
                  <p class="card-desc">
                    封装层支持传递 onUploadProgress 钩子，实时读取 progressEvent 计算百分比。
                  </p>
                  <div class="file-uploader">
                    <input type="file" ref="fileInputRef" @change="onFileSelected" />
                    <el-button type="primary" :disabled="!selectedFile" @click="onUploadFile">
                      上传选中的文件
                    </el-button>
                  </div>
                  <div v-if="uploadProgress > 0" class="progress-wrap">
                    <el-progress :percentage="uploadProgress" :status="uploadProgress === 100 ? 'success' : ''" />
                  </div>
                  <div v-if="uploadedResult" class="upload-result">
                    <el-tag type="success">上传成功！文件名: {{ uploadedResult.filename }}</el-tag>
                  </div>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">正常文件流下载 (Content-Disposition 解析)</span>
                  </template>
                  <p class="card-desc">
                    通过 Blob 接收流，从响应头 Content-Disposition 解码 UTF-8 中文文件名并触发浏览器保存。
                  </p>
                  <el-button type="success" @click="onDownloadNormalFile">
                    下载教学指南文本文件 (.txt)
                  </el-button>
                </el-card>

                <el-card shadow="hover" class="feature-card">
                  <template #header>
                    <span class="card-title">Blob 错误拦截捕获 (大厂高频面试坑)</span>
                  </template>
                  <p class="card-desc">
                    请求配置了 <code>responseType: 'blob'</code>，但后端报 500 业务错误。观察拦截器如何将二进制 Blob 读取为文本并解析出 JSON 错误提示，防止下载出破损文件！
                  </p>
                  <el-button type="danger" @click="onDownloadFailFile">
                    触发导出失败 (演示 Blob 捕获)
                  </el-button>
                </el-card>
              </div>
            </div>
          </el-tab-pane>

          <!-- TAB 6: 架构全景与教学总结 -->
          <el-tab-pane label="6. 架构解析与教学总结" name="arch">
            <div class="tab-content arch-content">
              <h3>Axios + TypeScript 企业级封装核心模块构成</h3>
              <el-descriptions border :column="2" class="arch-desc">
                <el-descriptions-item label="request.ts">
                  核心入口，创建主 service 与 refreshService，集成泛型 request&lt;T&gt;() 推导
                </el-descriptions-item>
                <el-descriptions-item label="types/axios.d.ts">
                  Axios 模块扩展声明，扩展 AxiosRequestConfig 支持 retryCount、showLoading、cancelDuplicate
                </el-descriptions-item>
                <el-descriptions-item label="cancel.ts">
                  基于 AbortController 实现根据请求指纹生成唯一 Key，自动取消重复未完成请求
                </el-descriptions-item>
                <el-descriptions-item label="loading.ts">
                  基于计数器模型 (Counter Pattern) 解决并发多个请求时 Loading 闪烁和过早关闭的难题
                </el-descriptions-item>
                <el-descriptions-item label="retry.ts">
                  接口失败根据 retryCount 和 retryDelay 进行重试，区分网络异常与 4xx 错误
                </el-descriptions-item>
                <el-descriptions-item label="token.ts">
                  双 Token 规范存储，管理短期 accessToken 与长期 refreshToken
                </el-descriptions-item>
                <el-descriptions-item label="download.ts">
                  Blob 二进制流下载，处理 RFC 5987 标准 UTF-8 响应头文件名解析与内存释放
                </el-descriptions-item>
              </el-descriptions>

              <h3 style="margin-top: 24px;">双 Token 无感刷新核心流程</h3>
              <div class="code-flow-card">
                <ol class="flow-list">
                  <li><strong>第 1 步:</strong> 页面发起业务请求，拦截器在 Header 携带短期 <code>accessToken</code>。</li>
                  <li><strong>第 2 步:</strong> 服务端校验发现 Token 过期，返回 <code>HTTP 401</code> 状态码。</li>
                  <li><strong>第 3 步:</strong> 响应错误拦截器捕获 401，判断 <code>isRefreshing</code> 锁是否已开启：
                    <ul>
                      <li>若已开启：将当前请求包装为 Promise 回调并塞入 <code>retryQueue</code> 队列中，等待广播唤醒；</li>
                      <li>若未开启：将 <code>isRefreshing = true</code>，使用无拦截器的 <code>refreshService</code> 请求 <code>/api/auth/refresh</code>；</li>
                    </ul>
                  </li>
                  <li><strong>第 4 步:</strong> 刷新成功：将新 Token 保存至 LocalStorage，遍历 <code>retryQueue</code> 队列把所有挂起的请求注入新 Token 并重新派发，最后重放原本触发 401 的请求；</li>
                  <li><strong>第 5 步:</strong> 刷新失败：清空队列与本地 Token，弹窗引导用户跳转至登录页。</li>
                </ol>
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>

      <!-- 右侧：实时日志与调用链路控制台 -->
      <aside class="console-sidebar">
        <RequestConsole />
      </aside>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { ElMessage } from 'element-plus';
import { useUserStore } from '@/stores/user';
import RequestConsole from '@/components/RequestConsole.vue';
import { clearAllPending } from '@/utils/cancel';
import { downloadFileByResponse } from '@/utils/download';
import { getDelayApi, getBusinessErrorApi, getHttpErrorApi, getRetryApi } from '@/api/test';
import { uploadFileApi, downloadFileApi, downloadFailApi } from '@/api/file';
import type { UserInfo, UploadResult } from '@/types/api';

const userStore = useUserStore();

const activeTab = ref<string>('basic');
const profileResult = ref<UserInfo | null>(null);
const tokenCountdown = ref<number>(0);
let countdownTimer: ReturnType<typeof setInterval> | null = null;

// 文件上传相关
const fileInputRef = ref<HTMLInputElement | null>(null);
const selectedFile = ref<File | null>(null);
const uploadProgress = ref<number>(0);
const uploadedResult = ref<UploadResult | null>(null);

// 慢请求相关
const isSlowLoading = ref<boolean>(false);

// 启动 Token 倒计时计时器
onMounted(() => {
  userStore.syncTokensFromStorage();
  countdownTimer = setInterval(() => {
    if (tokenCountdown.value > 0) {
      tokenCountdown.value--;
    }
  }, 1000);
});

onUnmounted(() => {
  if (countdownTimer) clearInterval(countdownTimer);
});

// 登录
async function handleQuickLogin(): Promise<void> {
  try {
    const res = await userStore.login('admin', '123456');
    tokenCountdown.value = res.expiresIn || 15;
    ElMessage.success('登录成功！已获取 15 秒短期 AccessToken');
  } catch (err: any) {
    ElMessage.error(err.message || '登录失败');
  }
}

// 退出
function handleLogout(): void {
  userStore.logout();
  tokenCountdown.value = 0;
  profileResult.value = null;
  ElMessage.info('已退出登录并清除本地 Token');
}

// 登录失败演示
async function onLoginError(): Promise<void> {
  try {
    await userStore.login('admin', 'wrong_password_999');
  } catch (err) {
    // 错误已被拦截器提示
  }
}

// 获取用户信息
async function onFetchUserProfile(): Promise<void> {
  try {
    const res = await userStore.fetchProfile();
    profileResult.value = res;
    ElMessage.success('获取用户信息成功！');
  } catch (err) {
    profileResult.value = null;
  }
}

// 携带全局 Loading 获取用户信息
async function onFetchUserProfileWithLoading(): Promise<void> {
  try {
    const res = await userStore.fetchProfile({
      showLoading: true,
      loadingText: '正在拉取用户专属数据，演示全局 Loading 遮罩...'
    });
    profileResult.value = res;
  } catch (err) {}
}

// ======================== TAB 2: 无感刷新 ========================
async function onTestSilentRefreshSingle(): Promise<void> {
  ElMessage.info('正在发起受保护请求...');
  try {
    const res = await userStore.fetchProfile();
    profileResult.value = res;
    ElMessage.success('请求成功！(如果先前过期，已由拦截器完成静默刷新并重放)');
    tokenCountdown.value = 15;
  } catch (err) {}
}

async function onTestConcurrentSilentRefresh(): Promise<void> {
  ElMessage.info('并发派发 5 个受保护请求，测试队列重放与去重刷新...');
  const promises = [1, 2, 3, 4, 5].map((idx) => {
    return userStore.fetchProfile({
      params: { _batchIndex: idx }
    });
  });

  try {
    const results = await Promise.all(promises);
    tokenCountdown.value = 15;
    ElMessage.success(`5 个并发请求全部成功完成！返回数据条数: ${results.length}`);
  } catch (err) {
    console.error('并发测试错误:', err);
  }
}

function onTestRefreshTokenExpired(): void {
  localStorage.setItem('AXIOS_DEMO_REFRESH_TOKEN', 'invalid_refresh_token_expired');
  userStore.syncTokensFromStorage();
  ElMessage.warning('已将本地 RefreshToken 置为无效伪造串，下一次 401 刷新将失败并提示退出登录');

  setTimeout(() => {
    userStore.fetchProfile();
  }, 300);
}

// ======================== TAB 3: 取消请求 ========================
async function onFastClickFiveTimes(): Promise<void> {
  ElMessage.info('正在瞬间发起 5 次 3 秒耗时接口...');
  for (let i = 1; i <= 5; i++) {
    getDelayApi({ delay: 3000 }).catch(() => {
      // 预料之中的取消
    });
    await new Promise((r) => setTimeout(r, 60));
  }
}

async function onStartSlowRequest(): Promise<void> {
  isSlowLoading.value = true;
  ElMessage.info('慢速请求已发起 (耗时 5 秒)，可点击【手动中断取消】');
  try {
    const res = await getDelayApi({ delay: 5000 });
    ElMessage.success(`慢速请求顺利返回：${res.message}`);
  } catch (err) {
    // 如果取消了
  } finally {
    isSlowLoading.value = false;
  }
}

function onCancelCurrentRequest(): void {
  clearAllPending('用户在界面点击了【手动中断取消】按钮！');
  isSlowLoading.value = false;
  ElMessage.warning('已触发 clearAllPending 取消当前请求');
}

async function onAllowConcurrentRequests(): Promise<void> {
  ElMessage.info('发起 3 个相同的请求 (配置 cancelDuplicate: false 允许并发)...');
  const list = [1, 2, 3].map(() => {
    return getDelayApi({ delay: 1500 }, { cancelDuplicate: false });
  });
  await Promise.all(list);
  ElMessage.success('3 个相同请求全部并发完成！');
}

// ======================== TAB 4: 错误与重试 ========================
async function onTestBusinessError(): Promise<void> {
  try {
    await getBusinessErrorApi();
  } catch (err) {}
}

async function onTestHttpError(status: number): Promise<void> {
  try {
    await getHttpErrorApi(status);
  } catch (err) {}
}

async function onTestAutoRetry(): Promise<void> {
  const clientId = 'client_' + Date.now();
  ElMessage.info('发起自动重试测试：服务端前 2 次返回 503，第 3 次自动重试成功！');
  try {
    const res = await getRetryApi(clientId);
    ElMessage.success(res.message);
  } catch (err) {}
}

// ======================== TAB 5: 文件上传与下载 ========================
function onFileSelected(e: Event): void {
  const target = e.target as HTMLInputElement;
  const files = target.files;
  if (files && files.length > 0) {
    selectedFile.value = files[0];
    uploadProgress.value = 0;
    uploadedResult.value = null;
  }
}

async function onUploadFile(): Promise<void> {
  if (!selectedFile.value) return;
  const formData = new FormData();
  formData.append('file', selectedFile.value);

  uploadProgress.value = 0;
  try {
    const res = await uploadFileApi(formData, (percent: number) => {
      uploadProgress.value = percent;
    });
    uploadedResult.value = res;
    ElMessage.success('文件上传成功！');
  } catch (err) {}
}

async function onDownloadNormalFile(): Promise<void> {
  ElMessage.info('开始请求二进制文件流...');
  try {
    const response = await downloadFileApi();
    downloadFileByResponse(response, '默认文件名.txt');
    ElMessage.success('文件下载成功，请查看浏览器下载栏！');
  } catch (err) {}
}

async function onDownloadFailFile(): Promise<void> {
  ElMessage.info('正在请求一个后端会报错的导出接口...');
  try {
    await downloadFailApi();
  } catch (err) {
    // 错误已被拦截器解析为 JSON 提示
  }
}
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #f8fafc;
  color: #1e293b;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 28px;
  background: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
}

.header-brand {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-icon {
  color: #3b82f6;
}

.brand-title {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: #0f172a;
}

.brand-subtitle {
  margin: 2px 0 0 0;
  font-size: 13px;
  color: #64748b;
}

.header-auth {
  display: flex;
  align-items: center;
  gap: 14px;
}

.token-timer {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  background: #f1f5f9;
  padding: 4px 10px;
  border-radius: 6px;
  color: #0284c7;
}

.token-timer.token-expired {
  background: #fee2e2;
  color: #ef4444;
}

.app-main {
  flex: 1;
  display: flex;
  padding: 16px 24px;
  gap: 18px;
  max-width: 1600px;
  margin: 0 auto;
  width: 100%;
  box-sizing: border-box;
}

.workbench {
  flex: 6;
  min-width: 0;
}

.console-sidebar {
  flex: 4;
  min-width: 380px;
  position: sticky;
  top: 16px;
  height: fit-content;
}

.demo-tabs {
  background: #ffffff;
  border-radius: 8px;
  min-height: 600px;
}

.tab-content {
  padding: 16px 8px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.token-status-banner {
  display: flex;
  gap: 24px;
  padding: 12px 16px;
  background: #f8fafc;
  border-radius: 6px;
  border: 1px dashed #cbd5e1;
}

.status-col {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
}

.status-col .label {
  font-weight: 600;
  color: #475569;
}

.action-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}

.feature-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-title {
  font-size: 14px;
  font-weight: 600;
  color: #1e293b;
}

.card-desc {
  font-size: 13px;
  color: #64748b;
  line-height: 1.5;
  margin-bottom: 14px;
}

.card-actions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.result-box {
  margin-top: 12px;
  background: #0f172a;
  color: #38bdf8;
  padding: 8px 12px;
  border-radius: 6px;
  max-height: 160px;
  overflow-y: auto;
  font-size: 12px;
}

.result-box pre {
  margin: 0;
}

.file-uploader {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.progress-wrap {
  margin-top: 10px;
}

.upload-result {
  margin-top: 10px;
}

.arch-desc {
  margin-top: 14px;
}

.code-flow-card {
  background: #ffffff;
  padding: 16px 20px;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.flow-list {
  padding-left: 20px;
  color: #334155;
  line-height: 1.8;
  font-size: 14px;
}

.flow-list code {
  background: #f1f5f9;
  padding: 2px 6px;
  border-radius: 4px;
  color: #0284c7;
  font-size: 13px;
}

@media (max-width: 1024px) {
  .app-main {
    flex-direction: column;
  }
  .console-sidebar {
    min-width: 100%;
    position: static;
  }
}
</style>
