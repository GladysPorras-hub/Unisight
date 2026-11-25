@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (
  echo Python no esta instalado. Descargalo en https://www.python.org y marca "Add Python to PATH".
  pause
  exit /b
)
echo Instalando dependencias, esto puede tardar la primera vez...
python -m pip install -q -r requirements.txt
echo Abriendo UNISIGHT en tu navegador. Cierra esta ventana para detenerla.
python -m streamlit run app.py
pause
