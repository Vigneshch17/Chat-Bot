import os

import anthropic
import streamlit as st

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    st.error("Set the ANTHROPIC_API_KEY environment variable before starting the app.")
    st.stop()

client = anthropic.Anthropic(api_key=api_key)

st.title("🤖 Claude AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=300,
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response.content[0].text
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    except anthropic.AuthenticationError:
        st.error("Anthropic rejected the API key. Replace ANTHROPIC_API_KEY with a valid key.")

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"👤 You: {msg['content']}")
    else:
        st.write(f"🤖 Bot: {msg['content']}")