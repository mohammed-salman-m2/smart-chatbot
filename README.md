# Chatbot using NLP Technologies

## Overview
This project implements a conversational AI chatbot named "Smart Chatbot" using Natural Language Processing (NLP) techniques. <br>
The chatbot is designed to understand various user inputs and provide meaningful responses based on predefined patterns. <br>
It leverages the power of `nltk` for natural language understanding, `scikit-learn` for machine learning-based text classification, and `streamlit` to offer an interactive web-based interface. <br>
This project demonstrates the integration of NLP with a user-friendly interface, suitable for personal or educational use.

---

## Features
- Detects and responds to user intents such as greetings, farewells, and expressions of gratitude.
- Provides dynamic responses that adapt to the user’s input.
- Displays a history of interactions for easy reference.
- Built using Python with integration of popular libraries for NLP and machine learning.

---

## Technologies Used
- **Python** (version 3.13.x)
- **NLTK (Natural Language Toolkit)** for text processing
- **Scikit-learn** for machine learning and data preprocessing
- **Streamlit** for the interactive web interface
- **JSON format** for storing and managing intents data

---

## Installation

### 1. Clone the Repository
- First, clone the repository to your local machine:
```bash
git clone https://github.com/mohammed-salman-m2/smart-chatbot.git

```
- Then navigate to the project directory:
```bash
cd smart-chatbot
```

### 2. Create a Virtual Environment (Optional but Recommended)
It is recommended to create a virtual environment to manage project dependencies.
- Create the virtual environment:

```bash
python -m venv venv
```
- Activate the virtual environment:
    - On Windows use:
      ```bash
      venv\Scripts\activate
      ```
    - On Linux/Mac use:
      ```bash
      source venv/bin/activate
      ```

### 3. Install Required Packages
Once the virtual environment is activated, install the required packages listed in `requirements.txt`

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
Before running the chatbot, download the necessary `NLTK` resources:

```python
import nltk
nltk.download('punkt')
```

---

## Usage
To run the chatbot application, execute the following command:
```bash
streamlit run app.py
```

Once the application is running, open your browser and interact with Smart Chatbot through the web interface. <br> Type your message in the input box, and hit Enter to see the chatbot's response. Example exchanges could look like:
* User: "Hello!"
* Chatbot: "Hi there! How can I help you today?"

---

## Intents Data
The chatbot’s behavior is controlled by the `intents.json` file, which defines different user intents, their matching patterns, and the appropriate responses. You can modify or expand this file to introduce new intents or adjust existing ones.

---

## Conversation History
The chatbot logs all interactions in a CSV file (`chat_log.csv`). This history allows users to review past conversations. <br>You can also view the conversation history by selecting the "Conversation History" option from the sidebar.

---

## Contributing
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request. <br> If you encounter any bugs or have feature suggestions, please open an issue.

---

## License
This project is licensed under the MIT License. See the [LICENSE]LICENSE file for details.

---

## Acknowledgments
- **NLTK** for Natural Language Processing.
- **Scikit-learn** for Machine Learning Algorithms.
- **Streamlit** for Building the Web Interface.

---


# Code the impossible, make it possible. 💻✨
