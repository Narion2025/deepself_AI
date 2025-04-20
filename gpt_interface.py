import openai, json, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("system_prompt.txt") as f:
    system_prompt = f.read()

with open("../logs/hume_output.json") as f:
    hume_data = json.load(f)

user_prompt = f"""Text: {hume_data.get("text", "Kein Text")}
Emotionen: {json.dumps(hume_data.get("emotions", {}), indent=2)}"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

with open("../logs/gpt_response.json", "w") as out:
    json.dump(response, out, indent=2)

print("✅ GPT-Antwort gespeichert.")
