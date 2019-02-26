# https://www.codewars.com/kata/most-frequently-used-words-in-a-text/python

'''
Write a function that, given a string of text (possibly with punctuation and
line-breaks), returns an array of the top-3 most occurring words, in 
descending order of the number of occurrences.

Assumptions:
    A word is a string of letters (A to Z) optionally containing one or more 
apostrophes (') in ASCII.
    Matches should be case-insensitive, and the words in the result should 
be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 
or top-1 words should be returned, or an empty array if a text contains no 
words.
'''

def top_3_words(text):

    # Remove punctuation from the input string by replacing\
    # it with space (replace with space to facilitate the\
    # split later)
    for punctuation in "|\\!@#£$§%€&/{([)]=}?*-+,;.:-_«»<>":
        text = text.replace(punctuation, ' ')
    # Separately replace triple primes
    text = text.replace("'''", ' ')

    # Create a list with all the words found in the input\
    # string (split at spaces)
    words_list = text.split()
    
    # # Convert the words to lowercase and include only non-empty strings
    # and 1-character strings of a prime ("'")
    words_list = [str(word.lower()) for word in words_list if word not in "'"]

    # Create a dictionary to hold the frequencies for each unique word\
    # in the words_list list
    word_counts = {word:words_list.count(word) for word in set(words_list)}
    
    # List to contain the 3 most frequent words    
    max_frequencies = list()

    # Run this loop 3 times because we are looking for the 3\
    # most frequent words
    for i in range(3):

        # Variables to keep track of what's the most frequent\
        # word and its frequency
        max_word, freq = '', 0
        
        # Loop through the dictionary of words and its frequencies\
        # to find the most frequent
        for word in word_counts:
            # If this word has a higher frequency than the most\
            # frequent word found so far, it becomes the most\
            # frequent word
            if word_counts[word] > freq:
                max_word, freq = word, word_counts[word]
        
        # If the most frequent word we found is not an empty\
        # string, then add it to the list of the 3 most\
        # frequent words and delete it from the dictionary\
        # so that we can find the next most frequent word
        if max_word != '':
            max_frequencies.append(max_word)
            del word_counts[max_word]

        # If the list doesn't have any words then break\
        # the loop because it means we don't have any\
        # words to return
        if len(max_frequencies) == 0:
            break

    return max_frequencies


import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])

    def test2(self):
        self.assertEqual(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])

    def test3(self):
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])

    def test4(self):
        self.assertEqual(top_3_words("  , e   .. "), ["e"])

    def test5(self):
        self.assertEqual(top_3_words("  ...  "), [])

    def test6(self):
        self.assertEqual(top_3_words("  '  "), [])

    def test7(self):
        self.assertEqual(top_3_words("  '''  "), [])

    def test8(self):
        self.assertEqual(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])


if __name__ == "__main__":
    unittest.main()