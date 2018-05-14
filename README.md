# spelling-corrector
a simple spelling corrector in [python](https://python.org). 
  
  
Based on the work of [Peter Norvig](http://norvig.com/).  
  
**Steps**:  
* run `generate_word_count.py` to create the `WORDS` pickle file.  
* run `unit_tests.py` to make sure all the tests pass.  
* run `spell_test.py` on the given test files and get the accuracy of the corrector.  
  
Note that the `datasets` directory contains the required data in `.txt` formats:  
* `big.txt` is a concatenation of public domain book excerpts from [Project Gutenberg](http://www.gutenberg.org/wiki/Main_Page) and lists of most frequent words from [Wiktionary](http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists) and the [British National Corpus](http://www.kilgarriff.co.uk/bnc-readme.html).  
* `spell-testset1.txt` and `spell-testset2.txt` are test files containing both correctly spelled words and their incorrect variations extracted from [Birkbeck spelling error corpus](http://ota.ahds.ac.uk/texts/0643.html)  
  
More info on the [algorithm](http://norvig.com/spell-correct.html).
