@echo off
echo Запуск Redis-сервера...
start "Redis Server" "C:\Program Files\Redis\redis-server.exe" "C:\Program Files\Redis\redis.windows.conf"

timeout /t 2 >nul

echo Запуск Flask-сервера...
start "Flask Server" cmd /k "cd backend && python app.py"

timeout /t 2 >nul

echo Запуск скрипта PowerShell для инициализации серверов...

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_all.ps1"

pause

