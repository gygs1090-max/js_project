@echo off
cd /d "%~dp0"
echo Pybo 서버 시작 중...
echo 브라우저: http://127.0.0.1:5000
echo 종료: Ctrl + C
echo.
vnavy\Scripts\python.exe run.py
pause
