@echo off
cd /d "%~dp0"
chcp 65001 >nul

echo ========================================================
echo   正在停止 Axios 教学项目相关后台服务（端口 3000 / 5173）
echo ========================================================
echo.

set FOUND=0

for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":3000 "') do (
    if not "%%a"=="0" (
        taskkill /f /pid %%a >nul 2>nul
        echo [已终止] 释放端口 3000 PID %%a
        set FOUND=1
    )
)

for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5173 "') do (
    if not "%%a"=="0" (
        taskkill /f /pid %%a >nul 2>nul
        echo [已终止] 释放端口 5173 PID %%a
        set FOUND=1
    )
)

echo.
echo ========================================================
echo   所有相关后台服务已成功清理释放！
echo ========================================================
echo.
pause
