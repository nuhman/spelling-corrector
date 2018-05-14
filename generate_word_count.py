from spell import words, get_count
import pickle

def get_word_count(TRAIN_FILE = 'big.txt'):    
    """
        End result: 
            {
                'the': 12839,
                'hello': 546,
                ....
            }
        Pickle the result.
    """
    WORDS = []
    with open(TRAIN_FILE) as f:
        _words = words(f.read())
        WORDS = get_count(_words)

    with open('WORDS.pickle', 'wb') as handle:
        pickle.dump(WORDS, handle)
    
if __name__ == '__main__':
    get_word_count()

