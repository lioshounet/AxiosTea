@echo off
chcp 65001 >nul
echo ========================================================
echo   正在启动 Axios 深度封装教学项目 (前端 + 后端)
echo ========================================================
echo [1/2] 正在启动 Node.js Express 后端服务 (端口: 3000)...
start "Node.js Backend [Port 3000]" cmd /k "cd server && npm start"
timeout /t 2 /nobreak >nul

echo [2/2] 正在启动 Vue 3 + Vite 前端开发服务器 (端口: 5173)...
start "Vue 3 Frontend [Port 5173]" cmd /k "cd client && npm run dev"

echo.
echo ========================================================
echo   项目已启动完毕！请在浏览器访问: http://localhost:5173
echo ========================================================
pause

