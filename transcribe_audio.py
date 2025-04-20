import whisper

model = whisper.load_model("base")
result = model.transcribe("../voice_input/input.wav")

with open("../logs/whisper_output.txt", "w") as f:
    f.write(result["text"])

print("✅ Transkription abgeschlossen.")
