import json, time

with open("../logs/gpt_response.json") as f:
    response = json.load(f)

log = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M"),
    "gpt_result": response
}

filename = f"../logs/entry_{int(time.time())}.json"
with open(filename, "w") as out:
    json.dump(log, out, indent=2)

print(f"✅ Log gespeichert: {filename}")
