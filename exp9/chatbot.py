import re
from collections import defaultdict

class SimilarityChatbot:
    def __init__(self, corpus_file):
        self.corpus = self.load_corpus(corpus_file)

    def load_corpus(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        corpus = [line.strip().lower() for line in lines if line.strip()]
        return corpus

    def tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def calculate_similarity(self, user_keywords, sentence):
        sentence_keywords = self.tokenize(sentence)
        return len(set(user_keywords).intersection(sentence_keywords))

    def get_most_similar_sentence(self, user_input):
        user_keywords = self.tokenize(user_input)
        best_match = None
        best_score = 0

        for sentence in self.corpus:
            score = self.calculate_similarity(user_keywords, sentence)
            if score > best_score:
                best_score = score
                best_match = sentence
        return best_match.capitalize() if best_match else "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Similarity-Based Chatbot!")
    print("Type 'bye' to exit the conversation.")
    corpus_file = "/home/csnn12/Desktop/Imthiyaz/exp9/exp9b.txt"  # Replace with your file path
    chatbot = SimilarityChatbot(corpus_file)   
    while True:
        user_input = input("You: ")
        if re.search(r"\b(bye|goodbye|see you)\b", user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a great day!")
            break
        print("Chatbot:", chatbot.get_most_similar_sentence(user_input))

if __name__ == "__main__":
    main()
