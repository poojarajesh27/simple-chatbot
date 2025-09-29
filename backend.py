from fastapi import FastAPI, Request
import uuid
from graph import run_agent

app = FastAPI()
SESSIONS = {}

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
    except Exception:
        return {"error": "Invalid or empty JSON payload."}

    user_message = data.get("message")
    if not user_message:
        return {"error": "Missing 'message' parameter."}

    session_id = data.get("session_id", str(uuid.uuid4()))

    if session_id not in SESSIONS:
        SESSIONS[session_id] = []

    SESSIONS[session_id].append(user_message)
    reply = run_agent(SESSIONS[session_id])
    SESSIONS[session_id].append(reply)

    return {"session_id": session_id, "reply": reply}
