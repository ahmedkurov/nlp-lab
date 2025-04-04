import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def named_entity_recognition(text):

    tokens = word_tokenize(text)
    

    tagged_tokens = pos_tag(tokens)
    

    named_entities = ne_chunk(tagged_tokens)
    
    return named_entities


sentence = input("Enter a sentence for Named Entity Recognition: ")


entities = named_entity_recognition(sentence)


print("\nNamed Entities:")
for subtree in entities:
    if isinstance(subtree, nltk.Tree):

        entity = " ".join(word for word, tag in subtree)
        label = subtree.label()
        print(f"{entity}: {label}")

