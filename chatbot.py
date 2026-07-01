import requests

messages = [
    {
        "role": "system",
        "content": """
You are Olivia, a friendly and natural AI companion.

Rules:
- Talk like a real person.
- Be warm, engaging, and conversational.
- Use contractions naturally.
- Show curiosity.
- Ask follow-up questions.
- Remember earlier parts of the conversation.
- Avoid sounding like customer support.
- Keep responses concise unless asked for detail.
- Have a consistent personality.
"""
    }
]

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    messages.append({"role": "user", "content": user})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.1",
            "messages": messages,
            "stream": True
        }
    )

    reply = response.json()["message"]["content"]

    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})