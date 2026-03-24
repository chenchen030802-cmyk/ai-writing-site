from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
CORS(app)  # 允许跨域访问

API_KEY = "sk-96e256b6d051414bac8dc49f9129ccfe"

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
