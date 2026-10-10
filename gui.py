import streamlit as st
from chatbot import get_response
from database import create_database, save_chat, get_chats, clear_chats
create_database()

st.set_page_config(
    page_title="AI College Chatbot",
    page_icon="🤖"
)

# Sidebar
st.sidebar.title("🤖 AI College Chatbot")

st.sidebar.write("### Features")
st.sidebar.write("✅ AI")
st.sidebar.write("✅ Machine Learning")
st.sidebar.write("✅ Computer Vision")
st.sidebar.write("✅ Python")
st.sidebar.write("✅ Chat History")

st.sidebar.write("---")

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    clear_chats()
    st.session_state.messages = []
    st.rerun()

# Title
st.title("🤖 AI College Chatbot")
st.caption("Ask me anything about AI, Python, Machine Learning and Computer Vision.")

# Name
name = st.text_input("👤 Enter your name")

# Session state

if "messages" not in st.session_state:
    st.session_state.messages = []

    chats = get_chats()

    for chat in chats:
        st.session_state.messages.append({
            "role": "user",
            "content": chat[1]
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": chat[2]
        })


# Show previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_message = st.chat_input("💬 Type your message...")

if user_message:

    if not name:
        st.warning("Please enter your name first.")
    else:

        # Show user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_message
        })

        with st.chat_message("user"):
            st.write(user_message)

        # Get bot response
        with st.spinner("🤖 Bot is thinking..."):
            response = get_response(user_message, name)

        # Show bot response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)

        # Save to database
        save_chat(user_message, response)
