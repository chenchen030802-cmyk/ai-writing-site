from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "sk-d3697987f941410aa8088d4e9b801c9a"

# 首页（返回网页）
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

# 生成文章接口
@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    type_ = data.get("type")
    content = data.get("content")

    prompt = f"请写一篇{type_}，主题：{content}，要求内容自然、结构清晰。"

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        result = response.json()
        text = result["choices"][0]["message"]["content"]

        return jsonify({"result": text})

    except Exception as e:
        return jsonify({"result": f"出错：{e}"})


if __name__ == "__main__":
    app.run()
