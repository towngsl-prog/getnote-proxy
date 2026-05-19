from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 你的配置（保持不变）
API_KEY = "gk_live_42875f21ce881a16.c4dcf4e0cf3c5b4272b159b631a4b826c5414f28829a811e"
CLIENT_ID = "cli_3802f9db08b811f197679c63c078bacc"
KNOWLEDGE_ID = "1n33X2rn"

@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json(silent=True) or {}
        query = data.get("query", "").strip()

        if not query:
            return jsonify({"code": 400, "error": "请输入问题"}), 400

        # Get 笔记官方 API
        url = "https://openapi.biji.com/open/api/v1/knowledge/recall"
        headers = {
            "Authorization": API_KEY,
            "X-Client-ID": CLIENT_ID,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        payload = {
            "knowledge_id": KNOWLEDGE_ID,
            "query": query,
            "top_k": 3
        }

        # 关键修复：增加超时 + 错误捕获
        resp = requests.post(url, headers=headers, json=payload, timeout=15)

        # 直接返回原始内容
        return resp.content, resp.status_code, {"Content-Type": "application/json"}

    except Exception as e:
        return jsonify({"code": 500, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
