

path = "/home/csnn12/Desktop/Imthiyaz/exp4/data.txt"


with open(path, encoding="utf-8") as file:
    text = file.read()


def sentence_tokenize(text):
    sentences = []
    temp_sentence = ""
    for char in text:
        temp_sentence += char
        if char in ".!?":
            sentences.append(temp_sentence.strip())
            temp_sentence = ""
    if temp_sentence:
        sentences.append(temp_sentence.strip())
    return sentences

dataset = sentence_tokenize(text)


def preprocess_text(text):
    cleaned_text = "".join(c if c.isalnum() or c.isspace() else " " for c in text)
    return " ".join(cleaned_text.split())

dataset = [preprocess_text(sentence) for sentence in dataset]


count = {}
def word_tokenize(sentence):
    return sentence.split()

for data in dataset:
    words = word_tokenize(data)
    for word in words:
        count[word] = count.get(word, 0) + 1


def get_top_words(count_dict, n=10):
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_items[:n]]

feature_names = get_top_words(count, 10)
print("Feature Names (Top 10 Words):", feature_names)


vectors = []
for data in dataset:
    words = word_tokenize(data)
    vector = [1 if word in words else 0 for word in feature_names]
    vectors.append(vector)

def print_table(feature_names, vectors):
    print("\nBinary Vectors:")
    print(" | ".join(["Sentences"] + feature_names))
    print("-" * (len(feature_names) * 10))
    for i, vector in enumerate(vectors):
        print(f"Sentence {i+1}" + " | " + " | ".join(map(str, vector)))

print_table(feature_names, vectors)

