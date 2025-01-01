path = '/home/csnn12/Desktop/Imthiyaz/exp2/data'

with open(path,'r') as file:
	text=file.read()
	
	# Remove Punctuation
	cleaned_text=""
	
	for char in text:
		if char.isalnum() or char.isspace():
			cleaned_text+=char
	
print(cleaned_text)
	
words=cleaned_text.split()

#total words
total_words = len(words)
print(f"Total words : {total_words}")


#unique words and word count

word_counts = {}
for word in words:
	if word in word_counts:
		word_counts[word] += 1
	else:
		word_counts[word] = 1
        
unique_words = len(word_counts)  # Number of unique words

print(f"Unique words : {unique_words}")
print("Word Count:")

for word,count in word_counts.items():
	print(f"{word} : {count}")
	

#TTR
typetoratio= (unique_words / total_words)*100
print(f"Type Token Ratio : {typetoratio:.2f}%")


