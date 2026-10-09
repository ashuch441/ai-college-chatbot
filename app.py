from database import create_database, save_chat, show_chats, clear_chats
import random
from datetime import datetime
from chatbot import get_response
print("Hello! I am your AI Chatbot.")
create_database()
name = input("What is your name? ")
print("Nice to meet you,", name)
while True:
    message = input("You: ")
    if message.lower() == "show chats":
        show_chats()
        continue
    if message.lower() == "clear":
        clear_chats()
        continue

    if message.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    try:
        response = get_response(message, name)
        print("Bot:", response)
        save_chat(message, response)

    except Exception as e:
       print("Bot: Sorry, something went wrong.")
       print("Error:", e)

    

    
  