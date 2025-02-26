@echo off
cd /d %~dp0
echo =============================================
echo 🚀 Setting up Python Virtual Environment...
echo =============================================

if not exist venv (
    echo 🔧 Creating Virtual Environment...
    python -m venv venv
)

echo activating virtual environment...
call venv\Scripts\activate

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