import speech_recognition as sr
import pyttsx3
import spacy

# Load spaCy
nlp = spacy.load("en_core_web_sm")

# Voice Engine
engine = pyttsx3.init()

engine.setProperty("rate", 170)

# ---------------------
# Speak
# ---------------------

def speak(text):

    print("Bot:", text)

    engine.say(text)
    engine.runAndWait()

# ---------------------
# Listen
# ---------------------

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:

            text = recognizer.recognize_google(audio)

            print("You:", text)

            return text.lower()

        except:

            return ""

# ---------------------
# NLP Chatbot
# ---------------------

def chatbot(user_text):

    doc = nlp(user_text)

    # Entity Detection

    for ent in doc.ents:

        print(
            f"Entity: {ent.text} -> {ent.label_}"
        )

    # Intent Matching

    if "hello" in user_text or "hi" in user_text:
        return "Hello, how can I help you?"

    elif "your name" in user_text:
        return "I am a voice assistant built using python and spacy."

    elif "machine learning" in user_text:
        return "Machine learning is a branch of artificial intelligence that learns patterns from data."

    elif "python" in user_text:
        return "Python is a popular programming language used in data science and artificial intelligence."

    elif "bye" in user_text:
        return "Goodbye have a nice day."

    else:
        return "Sorry, I did not understand your question."

# ---------------------
# Main Program
# ---------------------

speak("Voice assistant started")

while True:

    user_text = listen()

    if user_text == "":
        continue

    response = chatbot(user_text)

    speak(response)

    if "goodbye" in response.lower():
        break
