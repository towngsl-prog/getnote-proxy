from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "gk_live_42875f21ce881a16.c4dcf4e0cf3c5b4272b159b631a4b826c5414f28829a811e"
CLIENT_ID = "cli_3802f9db08b811f197679c63c078bacc"
KNOWLEDGE_ID = "1n33X2rn"

@app.route("/query", methods=["POST"])
def query():
    try:
        query = request.json.get("query", "")
        resp = requests.post(
            "https://openapi.biji.com/open/api/v1/knowledge/recall",
            headers={"Authorization": API_KEY, "X-Client-ID": CLIENT_ID, "Content-Type": "application/json"},
            json={"knowledge_id": KNOWLEDGE_ID, "query": query, "top_k": 3},
            timeout=10
        )
        return resp.json()
    except:
        return jsonify({"error": "api_error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
