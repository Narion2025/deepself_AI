#!/bin/bash

echo "🧠 Initialisiere DeepSelf Umgebung..."

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install requests openai python-dotenv

echo "✅ Umgebung fertig. Bitte fülle deine .env Datei aus!"

