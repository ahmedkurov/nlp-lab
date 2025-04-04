import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


file_paths = ["data1.txt", "data2.txt", "data3.txt"]


docs = [read_file(file) for file in file_paths]


vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(docs).toarray()


cosine_sim_matrix = cosine_similarity(bow_matrix)


print("Bag-of-Words Matrix:")
print(bow_matrix)

print("\nCosine Similarity Matrix:")
print(cosine_sim_matrix)
