from collections import Counter
import string
path = '/home/csnn12/Desktop/Imthiyaz/exp2/data'

with open(path,'r') as file:
	text=file.read()

text=text.translate(str.maketrans('','',string.punctuation))

words=text.split()

total_words = len(words)

word_counts= Counter(words)
unique_words= len(word_counts)
ttr= (unique_words/total_words)*100

#OUTPUT

print(f"Number of words in the file : {total_words}")
print(f"Number of unique words in the file : {unique_words}")

print("WORD COUNT :")

for word,count in word_counts.items():
	print(f"{word} : {count}")


print(f"Type to token ratio percentage: {ttr:.2f}%")
