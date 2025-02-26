@echo off
cd /d %~dp0
echo =============================================
echo 🚀 Setting up Python Virtual Environment...
echo =============================================

REM ✅ 가상환경(`venv`)이 없으면 생성
if not exist venv (
    echo 🔧 Creating Virtual Environment...
    python -m venv venv
)

REM ✅ `venv` 활성화
echo activating virtual environment...
call venv\Scripts\activate

REM ✅ 필요한 패키지 설치
echo =============================================
echo 📦 Installing required packages...
echo =============================================
pip install --upgrade pip
pip install -r requirements.txt

echo =============================================
echo ✅ Setup Complete! You can now run your program by run_program.bat or CMD.
echo =============================================

echo deactivating virtual environment...
call venv\Scripts\deactivate
pause