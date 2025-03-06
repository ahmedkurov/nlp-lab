import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line.strip()]


corpus_file = "data.txt"
corpus_sentences = read_corpus(corpus_file)


def find_most_similar_sentence(input_sentence, corpus_sentences):
    all_sentences = [input_sentence] + corpus_sentences

    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(all_sentences).toarray()

    cosine_similarities = cosine_similarity([bow_matrix[0]], bow_matrix[1:])[0]

    most_similar_index = np.argmax(cosine_similarities)
    most_similar_sentence = corpus_sentences[most_similar_index]
    similarity_score = cosine_similarities[most_similar_index]

    return most_similar_sentence, similarity_score


input_sentence = input("Enter a sentence: ")

most_similar_sentence, score = find_most_similar_sentence(input_sentence, corpus_sentences)

print("\nMost Similar Sentence from Corpus:")
print(f"'{most_similar_sentence}' (Similarity Score: {score:.2f})")

