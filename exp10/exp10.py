import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

class TextClassifier:
    def __init__(self, data_file):
    	self.data=pd.read_csv(data_file)
    	self.vectorizer=TfidfVectorizer()
    	self.model=MultinomialNB()
    	
    def preprocess_data(self):
        """Preprocess the dataset by splitting into training and testing sets."""
        self.data.dropna(inplace=True)  # Remove empty rows
        X = self.data['text'] # Ensure all text data is string
        y = self.data['SpamorNot']

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def train_model(self):
        """Train the text classifier using ."""
        X_train_tfidf = self.vectorizer.fit_transform(self.X_train)
        X_test_tfidf = self.vectorizer.transform(self.X_test)

        self.model.fit(X_train_tfidf, self.y_train)
        
        y_pred = self.model.predict(X_test_tfidf)
        print("\nModel Training Completed!")
        
      

    def classify_text(self, text):
        """Classify new text input using the ."""
        try:
            text_tfidf = self.vectorizer.transform([text])
            prediction = self.model.predict(text_tfidf)
            return prediction[0]
        except Exception as e:
            return f"Error processing input: {e}"

def main():
    print("Spam detection using TF-IDF and Naive Bayes!")
    data_file = "spam_detection.csv"  # Change this to the correct path
    
    classifier = TextClassifier(data_file)
    classifier.preprocess_data()
    
    print("\nTraining the model...")
    classifier.train_model()

    while True:
        user_input = input("\nEnter a sentence (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print(f"Prediction: {classifier.classify_text(user_input)}")

if __name__ == "__main__":
    main()

