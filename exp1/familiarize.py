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

"""download('punkt')
download('punkt_tab')
download('stopwords')
download('wordnet')"""

stemmer=PorterStemmer()
lemmatiser=WordNetLemmatizer()
stop_words=set(stopwords.words('english'))

"""def clean_text(text):
	
	print(f"plain text : {text}")
	
	text=text.lower()
	print(f"lowered text : {text}")
	
	text=re.sub(r'http\S+|www\S+|https\S+', '',text)
	print(f"link removed text : {text}")
	
	text=emoji.replace_emoji(text, replace='')
	print(f"emoji removed text : {text}")
	
	text=text.translate(str.maketrans('','',string.punctuation))
	print(f"punctuation removed text : {text}")
	
	words=word_tokenize(text)
	print(f"tokenized text : {words}")
	
	words=[word for word in words if word not in stop_words]
	print(f"stop words removed text : {words}")
	
	words=[stemmer.stem(word) for word in words]
	print(f"stemmer applied text : {words}")
	
	words=[lemmatiser.lemmatize(word) for word in words]
	print(f"lemmatized text : {words}")
	return ' '.join(words)"""
	
def clean(text):
	

	
	text=text.lower()

	
	text=re.sub(r'http\S+|www\S+|https\S+', '',text)

	
	text=emoji.replace_emoji(text, replace='')

	
	text=text.translate(str.maketrans('','',string.punctuation))

	
	words=word_tokenize(text)

	
	words=[word for word in words if word not in stop_words]

	
	words=[stemmer.stem(word) for word in words]

	
	words=[lemmatiser.lemmatize(word) for word in words]

	return ' '.join(words)
#main

path='/home/csnn12/Desktop/Imthiyaz/exp1/tweets'

with open(path,'r') as file:
	tweets=file.readlines()
	
"""for tweet in tweets:
	clean_text(tweet)"""
	
df=pd.DataFrame({'tweets':[tweet.strip() for tweet in tweets]})



df['cleaned_tweets']=df['tweets'].apply(clean)

print(df)



	

