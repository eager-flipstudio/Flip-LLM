from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BASE_URL = "https://llm-flip.vercel.app"

def R(data, status=200):
    return jsonify(data), status

def E(msg, status=400, **kw):
    return jsonify({"error": msg, **kw}), status

@app.route("/", methods=["GET"])
def index():
    return R({"name": "My AI App", "powered_by": BASE_URL})

@app.route("/models", methods=["GET"])
def models():
    r = requests.get(f"{BASE_URL}/models", timeout=10)
    return R(r.json(), r.status_code)

@app.route("/<model>/chat", methods=["GET", "POST"])
def chat(model):
    if request.method == "POST":
        body = request.get_json(silent=True) or {}
        text = body.get("text", "").strip()
        sid  = body.get("sid", "").strip() or None
    else:
        text = request.args.get("text", "").strip()
        sid  = request.args.get("sid", "").strip() or None

    if not text:
        return E("'text' is required", 400)

    params = {"text": text}
    if sid:
        params["sid"] = sid

    r = requests.get(f"{BASE_URL}/{model}/chat", params=params, timeout=60)
    return R(r.json(), r.status_code)

@app.route("/session/new", methods=["GET", "POST"])
def new_session():
    if request.method == "POST":
        body   = request.get_json(silent=True) or {}
        model  = body.get("model", "mistral-large-3")
        prompt = body.get("system_prompt", "")
        r = requests.post(f"{BASE_URL}/session/new", json={"model": model, "system_prompt": prompt}, timeout=10)
    else:
        model  = request.args.get("model", "mistral-large-3")
        prompt = request.args.get("system_prompt", "")
        r = requests.get(f"{BASE_URL}/session/new", params={"model": model, "system_prompt": prompt}, timeout=10)

    return R(r.json(), r.status_code)

@app.route("/session/<sid>/prompt", methods=["POST"])
def update_prompt(sid):
    body       = request.get_json(silent=True) or {}
    new_prompt = body.get("system_prompt", "")
    r = requests.post(f"{BASE_URL}/session/{sid}/prompt", json={"system_prompt": new_prompt}, timeout=10)
    return R(r.json(), r.status_code)

@app.route("/session/<sid>", methods=["GET"])
def session_info(sid):
    r = requests.get(f"{BASE_URL}/session/{sid}", timeout=10)
    return R(r.json(), r.status_code)

@app.route("/session/<sid>", methods=["DELETE"])
def delete_session(sid):
    r = requests.delete(f"{BASE_URL}/session/{sid}", timeout=10)
    return R(r.json(), r.status_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
