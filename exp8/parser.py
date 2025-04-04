import nltk
from nltk import CFG, PCFG
from nltk.parse import ChartParser, ViterbiParser

# Manually defined CFG (Context-Free Grammar)
cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> DT NN
    VP -> VB NP
    DT -> 'the' | 'a'
    NN -> 'dog' | 'cat' | 'man'
    VB -> 'chased' | 'saw'
""")

# Manually defined PCFG (Probabilistic Context-Free Grammar)
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> DT NN [0.6] | 'John' [0.4]
    VP -> VB NP [1.0]
    DT -> 'the' [0.5] | 'a' [0.5]
    NN -> 'man' [0.5] | 'cat' [0.5]
    VB -> 'chased' [0.6] | 'saw' [0.4]
""")

# Function for constituency parsing using the manually defined CFG
def constituency_parsing(sentence):
    """Performs constituency parsing using a manually defined CFG."""
    parser = ChartParser(cfg_grammar)
    words = sentence.lower().split()

    print("\nConstituency Parsing Trees:")
    parsed = parser.parse(words)
    for tree in parsed:
        print(tree)
        tree.pretty_print()

# Function for probabilistic parsing using the manually defined PCFG
def probabilistic_parsing(sentence):
    """Performs probabilistic parsing using a manually defined PCFG."""
    parser = ViterbiParser(pcfg_grammar)
    words = sentence.lower().split()

    print("\nProbabilistic Parsing Trees:")
    parsed = parser.parse(words)
    for tree in parsed:
        print(tree)
        tree.pretty_print()

# Get input from user
sentence = input("Enter a sentence (e.g., 'the dog chased a cat'): ")

# Run parsing functions
constituency_parsing(sentence)
probabilistic_parsing(sentence)

