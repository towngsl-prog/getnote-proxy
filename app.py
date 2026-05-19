from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ========== 你的信息（直接用你已有的） ==========
API_KEY = "gk_live_42875f21ce881a16.c4dcf4e0cf3c5b4272b159b631a4b826c5414f28829a811e"
CLIENT_ID = "cli_3802f9db08b811f197679c63c078bacc"
KNOWLEDGE_ID = "1n33X2rn"

@app.route("/query", methods=["POST"])
def query():
    try:
        query = request.json.get("query", "")
        if not query:
            return jsonify({"code": 400, "error": "请输入问题"})

        url = "https://openapi.biji.com/open/api/v1/knowledge/recall"
        headers = {
            "Authorization": API_KEY,
            "X-Client-ID": CLIENT_ID,
            "Content-Type": "application/json"
        }
        data = {
            "knowledge_id": KNOWLEDGE_ID,
            "query": query,
            "top_k": 3
        }

        resp = requests.post(url, headers=headers, json=data)
        return jsonify(resp.json())

    except Exception as e:
        return jsonify({"code": 500, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)