@echo off
cd /d "%~dp0"
chcp 65001 >nul

echo ========================================================
echo   Axios 工业级深度封装全栈实训教学项目一键启动
echo ========================================================
echo.

where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Node.js，请先安装 Node.js: https://nodejs.org/
    pause
    exit /b 1
)

where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 npm 命令，请检查环境变量 PATH。
    pause
    exit /b 1
)

if not exist "%~dp0server\node_modules" (
    echo [提示] 正在安装后端依赖包 npm install，请稍候...
    pushd "%~dp0server"
    call npm install
    popd
)

if not exist "%~dp0client\node_modules" (
    echo [提示] 正在安装前端依赖包 npm install，请稍候...
    pushd "%~dp0client"
    call npm install
    popd
)

echo [1/2] 正在启动后端 Express 服务（端口 3000）...
start "Node.js Backend [Port 3000]" /d "%~dp0server" cmd /k "npm start"

ping 127.0.0.1 -n 3 >nul

echo [2/2] 正在启动前端 Vue 3 + Vite 服务器（端口 5173）...
start "Vue 3 Frontend [Port 5173]" /d "%~dp0client" cmd /k "npm run dev"

echo.
echo ========================================================
echo   项目启动成功！
echo   - 前端页面: http://localhost:5173
echo   - 后端接口: http://localhost:3000
echo ========================================================
echo.
echo 正在自动在默认浏览器中打开页面...
ping 127.0.0.1 -n 3 >nul
start http://localhost:5173
exit /b 0
