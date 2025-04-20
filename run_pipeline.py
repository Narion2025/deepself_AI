import os

print("🚀 Starte DeepSelf Pipeline...")

os.system("python3 scripts/transcribe_audio.py")
os.system("python3 scripts/hume_connector.py")
os.system("python3 scripts/gpt_interface.py")
os.system("python3 scripts/memory_writer.py")

print("🏁 DeepSelf Lauf abgeschlossen.")
