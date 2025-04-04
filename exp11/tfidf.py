import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pandas as pd

def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_documents_from_directory(directory_path):
    documents = []
    file_names = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            documents.append(read_document(file_path))
            file_names.append(filename)
    return documents, file_names

def calculate_tfidf(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    return tfidf_matrix, feature_names

def display_transposed_tfidf_matrix(tfidf_matrix, feature_names, file_names):
    dense = tfidf_matrix.toarray()
    df = pd.DataFrame(
        data=dense.T,
        index=feature_names,
        columns=file_names
    )
    print("\nTF-IDF Matrix (Words as rows, Documents as columns):")
    print(df)
    csv_path = 'tfidf_matrix_transposed.csv'
    df.to_csv(csv_path)
    print(f"\nTransposed matrix saved to {csv_path}")
    return df

if __name__ == "__main__":
    directory_path = "/home/csnn12/Desktop/Imthiyaz/exp11/"
    documents, file_names = read_documents_from_directory(directory_path)
    
    if not documents:
        print("No documents found. Check your directory path.")
    else:
        tfidf_matrix, feature_names = calculate_tfidf(documents)
        transposed_matrix = display_transposed_tfidf_matrix(tfidf_matrix, feature_names, file_names)
        num_terms = len(feature_names)
        num_docs = len(file_names)
        print(f"\nMatrix dimensions: {num_terms} terms × {num_docs} documents")
        
        if num_terms > 20:
            print("\nSample of TF-IDF Matrix (first 20 terms):")
            print(transposed_matrix.iloc[:20, :])
