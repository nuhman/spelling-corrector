import pickle
import re
from collections import Counter

with open('WORDS.pickle', 'rb') as handle:
        WORDS = pickle.load(handle)

def words(text):
    """
        args:
            `text`: string
        returns:
            list of all the words in the `text`
    """
    return re.findall(r'\w+', text.lower())

def get_count(word_list):
    """
        args:
            `word_list`: list where each element is a string (word)
        returns:
            dictionary of counts for each word in `word_list`
    """
    return Counter(word_list)



def P(word): 
    """
        args:
            `word`: word for which we need to find probability (string)            
            `N`: the sum of all the word counts (integer)
        returns:
            Probability of the given `word` from the WORDS.
    """
    N=sum(WORDS.values())
    return WORDS[word] / N

def correction(word): 
    """
        argsmax function.
        args:
            `word`: string for which you need to find the correct word (spelling)
        returns:
            most probable spelling correction for the given 
            word based on the function `P`.
        
    """
    return max(candidates(word), key=P)

def candidates(word): 
    """
        Generate possible spelling corrections for `word`.
        Priorities:
            1. if the `word` is a known word in the `WORDS`.
            2. if the `word` is 'one edit` distant
            3. if the `word` is 'two edit` distant
            4. unknown word. So just return `word` back.
    """
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    """
        returns:
            the subset of `words` that appear in the dictionary of WORDS.
    """
    return set(w for w in words if w in WORDS)

def edits1(word):
    """
        returns:
            all edits that are one edit away from `word`.
    """
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    """
        returns:
            all edits that are two edits away from `word`.
    """
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))







    

