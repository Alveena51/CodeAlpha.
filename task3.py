#USE THIS TO RUN THE TASK ------- pip install nltk scikit-learn 
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

# Download necessary NLTK data
nltk.download('punkt')  # Tokenizer
nltk.download('wordnet')  # WordNet for synonyms

# Sample data for chatbot responses
chatbot_data = """
Hello! How can I help you today?
I can assist you with information about Python programming.
Python is a high-level, interpreted programming language.
It is widely used for web development, data analysis, artificial intelligence, and scientific computing.
Would you like to know more about a specific topic?
Python's syntax allows programmers to express concepts in fewer lines of code.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
You can use Python to automate tasks, analyze data, create machine learning models, and develop web applications.
Some popular Python libraries include NumPy, pandas, scikit-learn, TensorFlow, and Django.
Hello, I am here to help you. Ask me anything about Python.
Hi there! How can I assist you today?
"""

# Preprocess the text data
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Define chatbot responses
def chatbot_response(user_input):
    user_input = preprocess(user_input)
    responses = chatbot_data.strip().split('\n')
    responses = [preprocess(response) for response in responses]

    responses.append(user_input)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(responses)
    similarity_scores = cosine_similarity(tfidf[-1], tfidf[:-1])
    response_index = similarity_scores.argsort()[0][-1]
    response_score = similarity_scores[0, response_index]

    if response_score > 0.1:
        return chatbot_data.strip().split('\n')[response_index]
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Start chat function
def start_chat():
    print("Chatbot: Hello! How can I help you today? (type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chat()
