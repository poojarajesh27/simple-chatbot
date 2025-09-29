import streamlit as st
import requests
import uuid

st.title("Simple Local Chatbot")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip():
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "session_id": st.session_state["session_id"],
                "message": user_input
            }
        )
        data = response.json()
        if "reply" in data:
            st.text_area("Bot:", value=data["reply"], height=200)
        else:
            st.error(data.get("error", "Unknown error"))
    except Exception as e:
        st.error(f"Error sending request: {e}")
