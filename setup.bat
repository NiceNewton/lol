@echo off
echo 🚀 Setting up Low Light Image Enhancer...

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo 📍 Python version: %python_version%

REM Create virtual environment
echo 🔨 Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
echo 📦 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Check for model files
if not exist "models\LOW_LIGHT_MODEL.h5" (
    echo ⚠️  Model files not found in models\ directory
    echo 📝 Please ensure model files are placed in the models\ folder
)

echo ✅ Setup complete!
echo 🚀 Run the application with: streamlit run src/app.py
pause
