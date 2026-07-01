import streamlit as st
from groq import Groq

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Olivia AI",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
.stChatMessage {
    border-radius:15px;
}
footer {
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.title("🤖 Olivia AI")
    st.write("Your Human-like AI Assistant")

    st.markdown("---")

    st.write("### Model")
    st.success("Llama 3.3 70B")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": """
You are Olivia, a friendly, intelligent AI assistant.

Rules:
- Talk naturally.
- Give detailed answers.
- Be polite.
- Explain clearly.
- Use examples whenever possible.
"""
            }
        ]
        st.rerun()

    st.markdown("---")
    st.write("Made ❤️ by Kamakshi")

# -------------------------
# Title
# -------------------------
st.title("🤖 Olivia AI")
st.caption("Powered by Groq • Llama 3.3 70B")

# -------------------------
# Groq Client
# -------------------------
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("Groq API Key not found!")
    st.stop()

# -------------------------
# Initialize Chat
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are Olivia, a friendly AI companion.

Speak naturally.

Remember previous messages.

Be warm and engaging.
"""
        }
    ]

# -------------------------
# Display Chat
# -------------------------
for message in st.session_state.messages:
    if message["role"] != "system":
        avatar = "🤖" if message["role"] == "assistant" else "👤"

        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# -------------------------
# User Input
# -------------------------
prompt = st.chat_input("Ask me anything...")

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
                    max_tokens=1024,
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
                st.error(f"Error: {e}")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.caption("© 2026 Olivia AI | Developed by Kamakshi")
