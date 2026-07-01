
import streamlit as st
import requests

st.set_page_config(page_title="Olivia AI", page_icon="🤖")

st.title("🤖 AI by kamakshi" "")
st.write("Human-like chatbot powered by Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are Olivia, a friendly and natural AI companion.
Talk like a real person.
Be warm, engaging, and conversational.
Remember context from the conversation.
"""
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.1",
            "messages": st.session_state.messages,
            "stream": False
        }
    )

    bot_reply = response.json()["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)