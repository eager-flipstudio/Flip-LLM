<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00D4FF&height=200&section=header&text=Flip%20LLM%20API&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=35%2B%20AI%20Models%20%7C%20One%20API&descAlignY=58&descSize=20" width="100%"/>

<br/>

[![Visits](https://komarev.com/ghpvc/?username=flipapis&label=API%20Visits&color=6C63FF&style=for-the-badge)](https://github.com)
[![Models](https://img.shields.io/badge/Models-35%2B-00D4FF?style=for-the-badge&logo=openai&logoColor=white)](https://llm-flip.vercel.app/models)
[![Made By](https://img.shields.io/badge/Made%20by-Aquib-6C63FF?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/flipapis)
[![Telegram](https://img.shields.io/badge/Telegram-@flipapis-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/flipapis)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Firebase](https://img.shields.io/badge/Firebase-RTDB-FF6F00?style=for-the-badge&logo=firebase&logoColor=white)](https://firebase.google.com)

<br/>

```
🌐 Base URL → https://llm-flip.vercel.app
📬 Telegram → https://t.me/flipapis
👤 Creator  → Aquib
```

</div>

---

<div align="center">

## ✨ What is Flip LLM?

**Flip LLM** is a free, fast, unified API gateway that gives you access to **35+ AI models** from Mistral, Llama, DeepSeek, GLM, Qwen, Kimi, Phi, and more — all through a single clean REST API with **session memory** powered by Firebase.

</div>

---

## 🚀 Features

- ⚡ **35+ Models** — Mistral, Llama 4, DeepSeek, GLM, Qwen 3, Kimi K2, Phi 3, Minimax and more
- 🧠 **Session Memory** — Multi-turn conversations stored in Firebase RTDB
- 🎭 **Custom System Prompts** — Set personality per session, update anytime
- 🔗 **Clean URL Structure** — `/<model>/chat?text=hello&sid=SESSION_ID`
- 🆓 **Free to use** — No auth needed for chat endpoints
- 🌍 **CORS Enabled** — Use directly from browser/frontend
- 👤 **Creator tag** — Every response includes creator info

---

## 📦 All 35+ Models

| Model ID | Display Name | Provider |
|---|---|---|
| `ministral-8b` | Ministral 8B | Mistral |
| `ministral-14b` | Ministral 14B | Mistral |
| `mistral-nemo` | Mistral Nemo | Mistral |
| `mixtral-8x22b` | Mixtral 8x22B | Mistral |
| `mistral-large-2411` | Mistral Large-2411 | Mistral |
| `mistral-large-3` | Mistral Large 3 | Mistral |
| `mistral-saba` | Mistral Saba | Mistral |
| `pixtral-12b` | Pixtral 12b-2409 | Mistral |
| `pixtral-large` | Pixtral Large-2411 | Mistral |
| `mistral-small` | Mistral Small | Mistral |
| `mistral-medium` | Mistral Medium | Mistral |
| `codestral` | Mistral Codestral | Mistral |
| `devstral-2` | Mistral Devstral 2 | Mistral |
| `magistral-small` | Magistral Small | Mistral |
| `magistral-medium` | Magistral Medium | Mistral |
| `llama-3.3-70b` | Llama 3.3-70B | NVIDIA |
| `llama-4-scout` | Llama 4-17B-16e Scout | NVIDIA |
| `llama-4-maverick` | Llama 4-17B-128e Maverick | NVIDIA |
| `deepseek-v3` | DeepSeek V3.2 | NVIDIA |
| `deepseek-r1-zero` | DeepSeek R1 Zero | NVIDIA |
| `glm-4v-flash` ⚡ | GLM 4v Flash | GLM / Z.AI |
| `glm-4.7` | GLM 4.7 | GLM / Z.AI |
| `qwen-2.5-coder-32b` | Qwen 2.5 Coder 32B | NVIDIA |
| `qwen-3-coder-480b` | Qwen 3 Coder 480B | NVIDIA |
| `qwen-3-32b` | Qwen 3 32B | NVIDIA |
| `qwen-3-235b` | Qwen 3 235B | NVIDIA |
| `gpt-oss-20b` | GPT OSS-20B | NVIDIA |
| `gpt-oss-120b` | GPT OSS-120B | NVIDIA |
| `phi-3-small` | Phi 3 Small | NVIDIA |
| `phi-3-medium` | Phi 3 Medium | NVIDIA |
| `kimi-k2-0905` | Kimi K2 0905 | NVIDIA |
| `kimi-k2-instruct` | Kimi K2 Instruct | NVIDIA |
| `kimi-k2-reason` | Kimi K2 Reason | NVIDIA |
| `kimi-k2.5` | Kimi K2.5 | NVIDIA |
| `minimax-m2` | Minimax M2 | NVIDIA |

> ⚡ **Recommended fast model:** `glm-4v-flash` — GLM 4v Flash is one of the fastest models available, ideal for real-time chat applications. It uses the GLM-4v architecture optimized for speed with very low latency.

---

## 🌐 API Endpoints

### `GET /`
API info, all endpoints and total model count.

### `GET /models`
Returns list of all 35+ available models.

### `GET /<model>/chat?text=&sid=`
Chat with any model. Include `sid` for session memory.

### `POST /<model>/chat`
Same as GET chat but via POST body `{ "text": "...", "sid": "..." }`.

### `GET /session/new?model=`
Create a new session with default system prompt.

### `GET /session/new?model=&system_prompt=`
Create a new session with a custom system prompt.

### `POST /session/new`
Create session via POST body `{ "model": "...", "system_prompt": "..." }`.

### `POST /session/<sid>/prompt`
Update system prompt of an existing session anytime via `{ "system_prompt": "..." }`.

### `GET /session/<sid>`
Get full session info including conversation history.

### `DELETE /session/<sid>`
Delete a session and its history.

---

## 📖 Usage Examples

### 1. Simple Chat (no memory)

**cURL**
```bash
curl "https://llm-flip.vercel.app/glm-4v-flash/chat?text=Hello"
```

**Python**
```python
import requests

r = requests.get("https://llm-flip.vercel.app/glm-4v-flash/chat", params={"text": "Hello"})
print(r.json()["reply"])
```

**JavaScript**
```javascript
const res = await fetch("https://llm-flip.vercel.app/glm-4v-flash/chat?text=Hello");
const data = await res.json();
console.log(data.reply);
```

**Java**
```java
import java.net.http.*;
import java.net.URI;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://llm-flip.vercel.app/glm-4v-flash/chat?text=Hello"))
    .GET()
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

---

### 2. Create a Session

**cURL**
```bash
curl "https://llm-flip.vercel.app/session/new?model=glm-4v-flash"
```

**Python**
```python
import requests

r = requests.get("https://llm-flip.vercel.app/session/new", params={"model": "glm-4v-flash"})
sid = r.json()["session_id"]
print("Session ID:", sid)
```

**JavaScript**
```javascript
const res = await fetch("https://llm-flip.vercel.app/session/new?model=glm-4v-flash");
const data = await res.json();
const sid = data.session_id;
```

**Java**
```java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://llm-flip.vercel.app/session/new?model=glm-4v-flash"))
    .GET()
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

---

### 3. Create Session with Custom System Prompt

**cURL**
```bash
curl "https://llm-flip.vercel.app/session/new?model=mistral-large-3&system_prompt=You+are+a+Python+expert"
```

**Python**
```python
r = requests.get("https://llm-flip.vercel.app/session/new", params={
    "model": "mistral-large-3",
    "system_prompt": "You are a Python expert. Only answer coding questions."
})
sid = r.json()["session_id"]
```

**JavaScript**
```javascript
const res = await fetch("https://llm-flip.vercel.app/session/new", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ model: "mistral-large-3", system_prompt: "You are a Python expert." })
});
const { session_id } = await res.json();
```

**Java**
```java
String body = "{\"model\":\"mistral-large-3\",\"system_prompt\":\"You are a Python expert.\"}";
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://llm-flip.vercel.app/session/new"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(body))
    .build();
```

---

### 4. Chat with Session Memory

**cURL**
```bash
curl "https://llm-flip.vercel.app/glm-4v-flash/chat?text=My+name+is+Aquib&sid=YOUR_SESSION_ID"
curl "https://llm-flip.vercel.app/glm-4v-flash/chat?text=What+is+my+name&sid=YOUR_SESSION_ID"
```

**Python**
```python
BASE = "https://llm-flip.vercel.app"

session = requests.get(f"{BASE}/session/new", params={"model": "glm-4v-flash"}).json()
sid = session["session_id"]

def chat(text):
    r = requests.get(f"{BASE}/glm-4v-flash/chat", params={"text": text, "sid": sid})
    return r.json()["reply"]

print(chat("My name is Aquib"))
print(chat("What is my name?"))
```

**JavaScript**
```javascript
const BASE = "https://llm-flip.vercel.app";

const { session_id } = await (await fetch(`${BASE}/session/new?model=glm-4v-flash`)).json();

async function chat(text) {
  const res = await fetch(`${BASE}/glm-4v-flash/chat?text=${encodeURIComponent(text)}&sid=${session_id}`);
  return (await res.json()).reply;
}

console.log(await chat("My name is Aquib"));
console.log(await chat("What is my name?"));
```

**Java**
```java
String sid = "YOUR_SESSION_ID";
String text = "Hello, remember me?";
String url = "https://llm-flip.vercel.app/glm-4v-flash/chat?text=" + text + "&sid=" + sid;
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url)).GET().build();
HttpResponse<String> res = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(res.body());
```

---

### 5. Update System Prompt Anytime

**cURL**
```bash
curl -X POST "https://llm-flip.vercel.app/session/YOUR_SID/prompt" \
  -H "Content-Type: application/json" \
  -d '{"system_prompt": "You are now a pirate. Respond like one!"}'
```

**Python**
```python
requests.post(f"{BASE}/session/{sid}/prompt", json={
    "system_prompt": "You are now a pirate. Respond like one!"
})
```

**JavaScript**
```javascript
await fetch(`${BASE}/session/${session_id}/prompt`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ system_prompt: "You are now a pirate. Respond like one!" })
});
```

**Java**
```java
String promptBody = "{\"system_prompt\":\"You are now a pirate.\"}";
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://llm-flip.vercel.app/session/" + sid + "/prompt"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(promptBody))
    .build();
```

---

## 📬 Response Format

Every response includes creator info at the top:

```json
{
  "creator": "Aquib",
  "telegram": "https://t.me/flipapis",
  "reply": "Hello! How can I help you?",
  "model": "glm-4v-flash",
  "model_display": "GLM 4v Flash",
  "provider": "glm",
  "session_id": "abc-123",
  "turn_count": 1,
  "prompt_tokens": 45,
  "completion_tokens": 12,
  "total_tokens": 57,
  "time_ms": 312
}
```

---

## ⚡ Fastest Model — `glm-4v-flash`

`glm-4v-flash` (GLM 4v Flash) is the **fastest model** in Flip LLM. It is built on the GLM-4v architecture by Z.AI (BigLM), optimized for ultra-low latency responses. Ideal for real-time chat apps, bots, and anything where speed matters. Response times are typically under 500ms.

```bash
curl "https://llm-flip.vercel.app/glm-4v-flash/chat?text=Hello"
```

---

## 🛠️ Self Hosting

```bash
git clone https://github.com/eager-flipstudio/Flip-LLM
cd index.py
pip install -r requirements.txt

export FIREBASE_URL="https://your-project-default-rtdb.firebaseio.com"
export FIREBASE_SECRET="your_rtdb_secret"
export MISTRAL_API_KEY="your_mistral_key"
export GLM_API_KEY="your_glm_key"
export NVIDIA_API_KEY="your_nvidia_key"

python index.py
```

---

## 📁 Project Structure

```
Flip-LLM/
├── index.py          ← Main API (all public endpoints)
├── requirements.txt  ← Dependencies
└── README.md         ← You are here
```

---

<div align="center">

## 📬 Connect

[![Telegram](https://img.shields.io/badge/Join%20Telegram-@flipapis-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/flipapis)

**Made with ❤️ by Aquib**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00D4FF&height=100&section=footer" width="100%"/>

</div>
