import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="Olivia AI", page_icon="🤖")

st.title("🤖 AI by Kamakshi")
st.write("Human-like chatbot powered by Groq")

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize chat history
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

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages,
    )

    bot_reply = response.choices[0].message.content

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(bot_reply)
