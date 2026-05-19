from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 你的配置
API_KEY = "gk_live_42875f21ce881a16.c4dcf4e0cf3c5b4272b159b631a4b826c5414f28829a811e"
CLIENT_ID = "cli_3802f9db08b811f197679c63c078bacc"
KNOWLEDGE_ID = "1n33X2rn"

@app.route("/query", methods=["POST"])
def query():
    try:
        # 安全获取请求
        if not request.is_json:
            return jsonify({"code":400,"error":"必须传入JSON"}),400
            
        data = request.get_json()
        query = data.get("query", "").strip()
        if not query:
            return jsonify({"code":400,"error":"请输入问题"}),400

        # 调用 Get笔记 API（最强兼容版）
        url = "https://openapi.biji.com/open/api/v1/knowledge/recall"
        
        headers = {
            "Authorization": API_KEY,
            "X-Client-ID": CLIENT_ID,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        
        payload = {
            "knowledge_id": KNOWLEDGE_ID,
            "query": query,
            "top_k": 3
        }

        # 最稳的请求方式
        try:
            resp = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=20,
                verify=True  # 强制证书验证
            )
        except Exception as e:
            return jsonify({"code":500,"error":"请求Get笔记失败："+str(e)}),500

        # 直接原样返回给扣子，不做任何解析！
        return resp.text, resp.status_code, {"Content-Type": "application/json"}

    except Exception as e:
        return jsonify({"code":500,"error":"服务器错误："+str(e)}),500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
