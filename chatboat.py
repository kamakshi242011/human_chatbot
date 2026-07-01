import requests

conversation = [
    {
        "role": "system",
        "content": """
        You are Olivia, a friendly and human-like AI assistant.
        Talk naturally.
        Be warm and conversational.
        Ask follow-up questions.
        Remember previous messages.
        """
    }
]

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    conversation.append({
        "role": "user",
        "content": user
    })

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.1",
            "messages": conversation,
            "stream": False
        }
    )

    bot_reply = response.json()["message"]["content"]

    print("\nBot:", bot_reply, "\n")

    conversation.append({
        "role": "assistant",
        "content": bot_reply
    })