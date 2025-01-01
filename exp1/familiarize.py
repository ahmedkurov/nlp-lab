import re
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk import download
import emoji
nltk.download('punkt')       # For word tokenization
nltk.download('stopwords')   # For stopwords removal
nltk.download('wordnet')     # For lemmatization
# Initialize stemmer and lemmatizer for text normalization
stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

# Load stopwords for filtering out common words
stop_words = set(stopwords.words('english'))

# Function to clean and preprocess text
def clean(text):
    # Convert text to lowercase to ensure uniformity
    text = text.lower()

    # Remove URLs (http, https, and www)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # Replace emojis with an empty string
    text = emoji.replace_emoji(text, replace='')

    # Remove punctuation marks
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into individual words
    words = word_tokenize(text)

    # Remove stopwords (common, unimportant words)
    words = [word for word in words if word not in stop_words]

    # Apply stemming to reduce words to their root form
    words = [stemmer.stem(word) for word in words]

    # Apply lemmatization to reduce words to their base form
    words = [lemmatiser.lemmatize(word) for word in words]

    # Return the cleaned text as a single string
    return ' '.join(words)

# Main code to read, clean, and process tweets
path = '/home/csnn12/Desktop/Imthiyaz/exp1/tweets'

# Read the tweets from the specified file
with open(path, 'r') as file:
    tweets = file.readlines()

# Create a DataFrame to hold the raw and cleaned tweets
df = pd.DataFrame({'tweets': [tweet.strip() for tweet in tweets]})

# Apply the cleaning function to each tweet in the DataFrame
df['cleaned_tweets'] = df['tweets'].apply(clean)

# Print the DataFrame containing the cleaned tweets
print(df)
