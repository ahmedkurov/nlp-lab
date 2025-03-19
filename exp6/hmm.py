import nltk
import numpy as np
from nltk.tokenize import word_tokenize

# Download necessary NLTK data (run once)
try:
    nltk.data.find('taggers/universal_tagset')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('universal_tagset')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    
def train_hmm_tagger():
    """Train an HMM POS tagger using NLTK's built-in corpus."""
    # Use Brown corpus for training
    try:
        nltk.data.find('corpora/brown')
    except LookupError:
        nltk.download('brown')
    
    from nltk.corpus import brown
    
    # Get the tagged sentences from Brown corpus
    tagged_sentences = brown.tagged_sents(tagset='universal')
    
    # Train the HMM tagger
    hmm_tagger = nltk.HiddenMarkovModelTagger.train(tagged_sentences)
    
    return hmm_tagger

def pos_tag_sentence(sentence, hmm_tagger=None):
    """Tag a sentence with POS using the HMM tagger."""
    # Tokenize the input sentence
    tokens = word_tokenize(sentence)
    
    # Use the HMM tagger if provided, otherwise use NLTK's default tagger
    if hmm_tagger:
        tagged_tokens = hmm_tagger.tag(tokens)
    else:
        # Fallback to NLTK's default tagger if HMM tagger not available
        tagged_tokens = nltk.pos_tag(tokens, tagset='universal')
    
    return tagged_tokens

def display_pos_tags(tagged_tokens):
    """Display the POS tags in a neat tabular format."""
    print("\nPOS Tagging Results:")
    print("-" * 40)
    print(f"{'Word':<20} | {'POS Tag':<15}")
    print("-" * 40)
    
    for word, tag in tagged_tokens:
        print(f"{word:<20} | {tag:<15}")
    
    print("-" * 40)
    print("\nTag Meanings:")
    tag_meanings = {
        'NOUN': 'Noun',
        'VERB': 'Verb',
        'ADJ': 'Adjective',
        'ADV': 'Adverb',
        'PRON': 'Pronoun',
        'DET': 'Determiner',
        'ADP': 'Adposition',
        'NUM': 'Numeral',
        'CONJ': 'Conjunction',
        'PRT': 'Particle',
        'X': 'Other',
        '.': 'Punctuation'
    }
    
    for tag, meaning in tag_meanings.items():
        print(f"{tag:<6}: {meaning}")

def main():
    print("POS Tagging using Hidden Markov Model")
    print("====================================")
    
    # First time might take longer due to data downloads and training
    print("Initializing HMM tagger (this might take a moment)...")
    try:
        hmm_tagger = train_hmm_tagger()
        print("HMM tagger trained successfully!")
    except Exception as e:
        print(f"Couldn't train HMM tagger: {e}")
        print("Falling back to NLTK's default tagger.")
        hmm_tagger = None
    
    while True:
        # Get input from user
        user_input = input("\nEnter a sentence (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
        
        # Process the sentence
        tagged_tokens = pos_tag_sentence(user_input, hmm_tagger)
        
        # Display results
        display_pos_tags(tagged_tokens)

if __name__ == "__main__":
    main()
