# Проверка и установка Chocolatey
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Output "Установка Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# Установка Redis
if (-not (Test-Path "C:\Program Files\Redis\redis-server.exe")) {
    Write-Output "Установка Redis..."
    choco install redis-64 -y
}

# Проверка наличия Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python не найден. Установите Python вручную."
    exit
}

# Создание виртуального окружения и установка зависимостей
if (-not (Test-Path ".\myenv")) {
    Write-Output "Создание виртуального окружения и установка Flask/Redis..."
    python -m venv myenv
    .\myenv\Scripts\activate
    pip install flask redis
} else {
    .\myenv\Scripts\activate
}

# Запуск Redis-сервера
Start-Process "C:\Program Files\Redis\redis-server.exe" "C:\Program Files\Redis\redis.windows.conf"

Start-Sleep -Seconds 2

# Запуск Flask-приложения
Start-Process powershell -ArgumentList "cd backend; . ..\myenv\Scripts\activate; python app.py"
