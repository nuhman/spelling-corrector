from spell import correction, WORDS

def make_testset(lines):
    """
        Check test files ('spell-testset1.txt') for the format of the file.
        Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs.
    """
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]

def spell_test(tests, verbose=False):
    """
        Run correction(wrong) on all (right, wrong) pairs.
        No return statement; just report results.
    """        
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))    
    print('{:.0%} of {} correct ({:.0%} unknown)'
          .format(good / n, n, unknown / n))
    

def start_test(test_file):
    with open(test_file) as f:
        spell_test(make_testset(f))

if __name__ == '__main__':
    start_test('spell-testset1.txt')
