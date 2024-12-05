import os
import json
import datetime
import csv
import nltk # type: ignore
import ssl
import streamlit as st # type: ignore
import random
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter
    st.title("Intents of Chatbot by using NLP")

    # Create a sidebar menu with options
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home Menu
    if choice == "Home":
        st.write("Welcome to the chatbot! Type your message and press Enter to begin chatting. 😊")

        # Check if the chat_log.csv file exists, and if not, create it with column names
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You: ", key=f"user_input_{counter}")

        if user_input:

            # Convert the user input to a string
            user_input_str = str(user_input)

            response = chatbot(user_input)
            st.text_area("Chatbot: ", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

            # Save the user input and chatbot response to the chat_log.csv file
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting with me! Wishing you a wonderful day ahead! 😊")
                st.stop()

    # Conversation History Menu
    elif choice == "Conversation History":
        # Display the conversation history in a collapsible expander
        st.header("Conversation History")
        # with st.beta_expander("Click to see Conversation History"):
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")

    # About page

    elif choice == "About":
        st.write("The goal of this project is to create a chatbot that can understand and reply to what users say based on their intentions. The chatbot uses the Natural Language Processing (NLP) library and Logistic Regression to identify the user's intentions and important information. The chatbot is made with Streamlit, a Python library used to create interactive web apps.")

        st.subheader("Project Overview:")

        st.write("""
        The project is split into two parts:
        1. NLP techniques and the Logistic Regression algorithm are used to teach the chatbot to recognize labeled intentions and key information.
        2. Streamlit is used to create a web-based chatbot interface where users can type text and get responses from the chatbot.
        """)

        st.subheader("Dataset:")

        st.write("""
        The dataset used in this project consists of labeled intents and entities, stored in a list.
        - Intents: These are the goals or purposes behind the user's input (e.g., "greeting", "budget", "about").
        - Entities: These are specific pieces of information taken from the user's input (e.g., "Hi", "How do I create a budget?", "What is your purpose?").
        - Text: This is the actual text the user types.
        """)

        st.subheader("Streamlit Chatbot Interface:")

        st.write("The chatbot interface is created with Streamlit. It has a text input box where users can type their messages and a chat window that shows the chatbot's responses. The interface uses the trained model to generate replies based on what the user types.")

        st.subheader("Conclusion:")

        st.write("In this project, a chatbot is created that understands and responds to user input based on their intentions. The chatbot is trained using NLP and Logistic Regression, and its interface is built with Streamlit. This project can be expanded by adding more data, using advanced NLP techniques, and incorporating deep learning algorithms.")

if __name__ == '__main__':
    main()
