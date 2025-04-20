from flask import Flask, request, render_template
import os, time

UPLOAD_FOLDER = 'voice_input'
LOG_FOLDER = 'logs'

# 📂 Ordner sicherstellen
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['audio']
        if file and file.filename.endswith('.wav'):
            filename = f"input_{int(time.time())}.wav"
            filepath = os.path.join(UPLOAD_FOLDER, "input.wav")
            file.save(filepath)

            os.system("python3 scripts/run_pipeline.py")

            with open(f"{LOG_FOLDER}/gpt_response.json", "r") as f:
                result = f.read()

            return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == '__main__':
    app.run(debug=True)
