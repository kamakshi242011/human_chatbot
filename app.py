import streamlit as st
from groq import Groq

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="K_AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.stChatMessage {
    border-radius:15px;
}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:

    st.title("🤖 K_AI")

    st.write("Human-like AI Assistant")

    st.markdown("---")

    st.success("Model: Llama 3.3 70B")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = [
            {
                "role":"system",
                "content":"""
You are Olivia, a friendly AI assistant.

Talk naturally.

Give detailed answers.

Be helpful.

Remember previous conversation.
"""
            }
        ]

        st.rerun()

    st.markdown("---")

    st.write("👨‍💻 Developed by Kamakshi")

# -------------------------------
# Title
# -------------------------------
st.title("🤖  K_AI")

st.caption("Powered by Groq • Llama 3.3 70B")

# -------------------------------
# Groq Client
# -------------------------------
try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except Exception:
    st.error("⚠️ Please add GROQ_API_KEY in Streamlit Secrets.")
    st.stop()

# -------------------------------
# Session State
# -------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role":"system",

            "content":"""
You are Olivia.

Be friendly.

Be intelligent.

Explain everything clearly.

Use examples whenever useful.
"""
        }

    ]

# -------------------------------
# Display Previous Messages
# -------------------------------
for msg in st.session_state.messages:

    if msg["role"] != "system":

        avatar = "🤖" if msg["role"]=="assistant" else "👤"

        with st.chat_message(msg["role"], avatar=avatar):

            st.markdown(msg["content"])

# -------------------------------
# Chat Input
# -------------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user", avatar="👤"):

        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Olivia is thinking..."):

            try:

                response = client.chat.completions.create(

                    model="llama-3.3-70b-versatile",

                    messages=st.session_state.messages,

                    temperature=0.7,

                    max_tokens=1024

                )

                reply = response.choices[0].message.content

                st.markdown(reply)

                st.session_state.messages.append(
                    {
                        "role":"assistant",
                        "content":reply
                    }
                )

            except Exception as e:

                st.error(f"Error : {e}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")

st.caption("© 2026 Olivia AI | Developed by Kamakshi")

                
