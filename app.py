from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "这里填你的DeepSeek API Key"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    type_ = data.get("type")
    content = data.get("content")

    prompt = f"请写一篇{type_}，主题是：{content}，内容自然，结构清晰"

    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()
    text = result["choices"][0]["message"]["content"]

    return jsonify({"result": text})
