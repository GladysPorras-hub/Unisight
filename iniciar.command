#!/bin/bash
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null; then
  echo "Python no esta instalado. Descargalo en https://www.python.org"
  read -p "Presiona Enter para salir"; exit 1
fi
echo "Instalando dependencias, esto puede tardar la primera vez..."
python3 -m pip install -q -r requirements.txt
echo "Abriendo UNISIGHT en tu navegador. Cierra esta ventana para detenerla."
python3 -m streamlit run app.py
