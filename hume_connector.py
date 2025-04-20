import requests, json, os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("HUME_API_KEY")
AUDIO_PATH = "../voice_input/input.wav"
OUTPUT_PATH = "../logs/hume_output.json"

with open(AUDIO_PATH, "rb") as f:
    files = {'file': f}
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.post("https://api.hume.ai/v0/stream/models/evi", headers=headers, files=files)

with open(OUTPUT_PATH, "w") as out:
    json.dump(response.json(), out, indent=2)

print("✅ Hume AI Analyse abgeschlossen.")
