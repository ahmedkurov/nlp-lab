import string
from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.corpus import stopwords

# Path to the input text file
path = "/home/csnn12/Desktop/Imthiyaz/exp3/data"

# Load English stopwords
stop_words = set(stopwords.words('english'))

def generate_concordance(text, context_window):
    """
    Generates a concordance (word-in-context) display for a selected word within a given context window.
    
    Parameters:
    text (str): The input text to process.
    context_window (int): The number of words to display before and after the target word.
    """
    # Store the original text
    original_text = text
    
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Tokenize text into words
    words = text.split()
    
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Lemmatize words to their base forms
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    
    # Count occurrences of each lemmatized word
    word_counts = Counter(lemmatized_words)
    
    # Display words occurring at least 3 times
    print("Options: ")
    for word, count in word_counts.items():
        if count >= 3:
            print(f"{word} : {count}")
    
    # User input for target word
    select = input("Enter the word you need: ")

    concordances = []

    # Find occurrences of the selected word and extract its context
    for i, word in enumerate(lemmatized_words):
        if word == select:
            start = max(i - context_window, 0)
            end = min(i + 1 + context_window, len(lemmatized_words))
            original_sentence = ' '.join(words[start:i]) + ' [' + words[i] + '] ' + ' '.join(words[i + 1:end])
            concordances.append(original_sentence)
    
    # Display results
    if concordances:
        print("\nContext window results:")
        for concordance in concordances:
            print(concordance)
    else:
        print(f"No occurrences of the word '{select}' found.")

# Read text from the file
with open(path) as file:
    text = file.read()

# User input for context window size
window = int(input("Enter the context window: "))

# Call the concordance generator function
generate_concordance(text, window)

