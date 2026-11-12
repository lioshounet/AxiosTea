<template>
  <div class="request-console">
    <div class="console-header">
      <div class="header-left">
        <span class="pulse-dot"></span>
        <span class="title">Axios 拦截器执行链路与实时日志 (TypeScript 教学观察台)</span>
        <el-tag size="small" type="info">已记录 {{ loggerStore.logs.length }} 条</el-tag>
        <el-tag size="small" type="warning" v-if="pendingCount > 0">
          Pending 请求: {{ pendingCount }}
        </el-tag>
      </div>
      <div class="header-right">
        <el-button size="small" type="danger" text @click="loggerStore.clearLogs">清空控制台</el-button>
      </div>
    </div>

    <div class="console-body" ref="logContainerRef">
      <div v-if="loggerStore.logs.length === 0" class="empty-tip">
        暂无请求活动，点击上方测试按钮体验各类封装场景...
      </div>

      <div
        v-for="log in loggerStore.logs"
        :key="log.id"
        :class="['log-item', `log-${log.type}`]"
      >
        <div class="log-meta">
          <span class="log-time">{{ log.time }}</span>
          <el-tag :type="getTagType(log.type)" size="small" effect="dark" class="log-tag">
            {{ log.type.toUpperCase() }}
          </el-tag>
          <span class="log-title">{{ log.title }}</span>
        </div>
        <div class="log-content">{{ log.content }}</div>
        <div v-if="log.payload" class="log-payload">
          <pre><code>{{ JSON.stringify(log.payload, null, 2) }}</code></pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { useLoggerStore } from '@/stores/logger';
import { getPendingCount } from '@/utils/cancel';
import type { LogItem } from '@/types/api';

const loggerStore = useLoggerStore();
const pendingCount = ref<number>(0);
let timer: ReturnType<typeof setInterval> | null = null;

onMounted(() => {
  timer = setInterval(() => {
    pendingCount.value = getPendingCount();
  }, 300);
});

onUnmounted(() => {
  if (timer) clearInterval(timer);
});

function getTagType(type: LogItem['type']): 'success' | 'danger' | 'warning' | 'info' {
  switch (type) {
    case 'success':
      return 'success';
    case 'error':
      return 'danger';
    case 'warning':
      return 'warning';
    default:
      return 'info';
  }
}
</script>

<style scoped>
.request-console {
  display: flex;
  flex-direction: column;
  background-color: #1e1e24;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  font-family: 'Consolas', 'Monaco', monospace;
  height: 480px;
}

.console-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  background: #2b2b36;
  border-bottom: 1px solid #3d3d4e;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.pulse-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.title {
  color: #f1f5f9;
  font-size: 13px;
  font-weight: 600;
}

.console-body {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.empty-tip {
  color: #64748b;
  text-align: center;
  margin-top: 140px;
  font-size: 14px;
}

.log-item {
  padding: 8px 12px;
  border-radius: 6px;
  background-color: #262633;
  border-left: 4px solid #64748b;
  font-size: 13px;
}

.log-item.log-success { border-left-color: #10b981; }
.log-item.log-error { border-left-color: #ef4444; }
.log-item.log-warning { border-left-color: #f59e0b; }
.log-item.log-info { border-left-color: #3b82f6; }

.log-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.log-time {
  color: #94a3b8;
  font-size: 11px;
}

.log-tag {
  font-size: 10px;
  padding: 0 4px;
  height: 18px;
  line-height: 18px;
}

.log-title {
  color: #f8fafc;
  font-weight: bold;
}

.log-content {
  color: #cbd5e1;
  line-height: 1.4;
  word-break: break-all;
}

.log-payload {
  margin-top: 6px;
  background: #18181f;
  padding: 6px 10px;
  border-radius: 4px;
  overflow-x: auto;
}

.log-payload pre {
  margin: 0;
  color: #38bdf8;
  font-size: 11px;
}
</style>
