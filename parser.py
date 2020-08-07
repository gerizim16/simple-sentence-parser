import nltk
import sys
import re
from queue import SimpleQueue

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to" | "until"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> S Conj S | S P S | NP VP | S Adv

NP -> NP Conj NP | N | AdjP NP | NP PP | Det N | Det AdjP N
VP -> VP Conj VP | V | V NP | V PP | AdvV | AdvV NP | AdvV PP
AdjP -> Adj | Adj AdjP
AdvV -> Adv V | V Adv
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    """
    tokens = nltk.word_tokenize(sentence)
    tokens = (word.lower() for word in tokens if re.search('[a-zA-Z]', word))
    return list(tokens)


def np_chunk_recursive(tree, chunks):
    """
    Helper function for np_chunk
    Returns true if there is an NP subtree else False
    """
    # Base case
    if type(tree) == str:
        return False

    # Recursion
    np_subtree = False
    for child_tree in tree:
        if np_chunk_recursive(child_tree, chunks):
            np_subtree = True

    if not np_subtree and tree.label() == 'NP':
        chunks.append(tree)
        np_subtree = True

    return np_subtree


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = list()
    np_chunk_recursive(tree, chunks)
    return chunks


if __name__ == "__main__":
    main()
