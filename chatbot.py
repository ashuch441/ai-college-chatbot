from datetime import datetime
def get_response(message, name):
    message = message.lower()
    if message in ["hello", "hi", "hey"]:
        return f"Hello {name}! How are you?"


    elif message in [
        "howare you",
        "how are you doing",
         "how r u",
         "i am fine",
         "i am fine and you",
         "i am fine and u",
         "i'm fine",
         "i'm fine and you",
         "i'm fine and u" 
]:
        return f"I am fine too, {name}! 😊 How can I help you?"
    elif message in ["what is your name", "tumhara naam kya hai"]:
        return "Mera naam Python Bot hai."
    elif message in [
       "what is ai",
       "ai kya hai",
       "ai kya hota hai",
       "tell me about ai",
       "artificial intelligence",
       "ai"

]:
       return "AI ka matlab Artificial Intelligence hai. AI computers ko intelligent tasks karne mein help karta hai."
    elif message in [
       "what is machine learning",
       "machine learning kya hai",
       "ml kya hai",
       "what is ml",
       "ml"
]:
       return "Machine Learning AI ka ek part hai jisme computer data se patterns learn karta hai."
    elif message in [
       "what is computer vision",
       "computer vision kya hai",
       "cv kya hai",
       "cv"
]:
       return "Computer Vision computers ko images aur videos ko understand karne mein help karta hai."

    elif message in ["what is python", "python kya hai"]:
        return "Python ek programming language hai."

    elif message == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        return "Current time is " + current_time

    elif message == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        return "Today's date is " + today
    elif message == "help":
        return """I can help you with:
1. AI
2. Machine Learning
3. Computer Vision
4. Python
5. B.Tech
6. AIML
7. Time and Date
8. Chat History
9. College Project"""
    elif message == "good morning":
        return f"Good morning, {name}! Have a great day."

    elif message == "good night":
        return f"Good night, {name}! Sweet dreams."

    elif message in ["thanks", "thank you"]:
        return f"You're welcome, {name}!" 
    elif message in ["what can you do", "tum kya kar sakte ho"]:
        return "Main AI, Machine Learning, Computer Vision, Python aur basic college-related questions mein help kar sakta hoon."

    elif message in ["who created you", "tumhe kisne banaya"]:
        return "Mujhe Python ka use karke ek college project ke roop mein banaya gaya hai."

    elif message in ["what is your purpose", "tumhara purpose kya hai"]:
        return "Mera purpose students ko basic information aur learning mein help karna hai." 
    elif message in ["what is btech", "btech kya hai"]:
        return "B.Tech ek undergraduate engineering degree hai."

    elif message in ["what is ai ml", "aiml kya hai"]:
        return "AI and ML ka matlab Artificial Intelligence and Machine Learning hai."

    elif message in ["what is computer science", "computer science kya hai"]:
        return "Computer Science computers, software, algorithms aur programming ka study hai."

    elif message in ["what is college project", "college project kya hai"]:
        return "College project ek practical project hota hai jisme students apni technical knowledge ko apply karte hain."  

    elif message == "menu":
        return """Available commands:
- AI
- Machine Learning
- Computer Vision
- Python
- B.Tech
- AIML
- Time
- Date
- Help
- Show chats
- Bye"""
    elif message == "clear":
        return "Chat history clear karne ke liye database function add karenge."
    else:
        return "I am still learning. Please ask me something about AI, Python, Machine Learning, or Computer Vision."