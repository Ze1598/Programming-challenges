# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/solutions/python

# Functions to count letter instances totals in a word and compare\
# words for to find anagrams

# Function to count letter instances totals in a single word
def count_letters(word):
    # Dictionary to contain the different letters and their counts
    word_letters = {}
    # Loop through the word; each time a "new" letter is found, add it to\
    # the dictionary with a value of 1 (1 instance); each time a letter
    # is repeated, increment it in the dictionary
    for i in word:
        if i not in word_letters:
            word_letters[i] = 1
        else:
            word_letters[i] += 1

    print(f'Letter counts for "{word}":\n{word_letters}')
    return word_letters

print('Basic word count:')
count_letters('abba')
count_letters('racer')
print()

# My first solution
# The main difference here to the second solution is that here I use\
# to main dictionaries: the first for the input word letter counts\
# and a second one to contain all the counts for each test word. In\
# the end I return a list with the anagrams
def anagrams(word, words):
    # Letter instances in word
    word_counts = {}
    # Letters instances in each test word
    words_counts = {}
    # Counts for the single word
    for letter in word:
        if letter in word_counts:
            word_counts[letter] += 1
        else:
            word_counts[letter] = 1
    
    # Counts for the test words
    for test in words:
        words_counts[test] = {}
        for letter in test:
            if letter in words_counts[test]:
                words_counts[test][letter] += 1
            else:
                words_counts[test][letter] = 1

    return sorted([word for word in words_counts if words_counts[word] == word_counts])

print('Solution 1')
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print()


# A second, more optimized, solution
def anagrams(word, words):
    # Letter counts in word
    word_counts = {}
    # Will contain only words that are anagrams of 'word'
    matches = []

    # Letter counts for the single word
    for letter in word:
        if letter in word_counts:
            word_counts[letter] += 1
        else:
            word_counts[letter] = 1
    
    # Counts for the test words (loop through the list of input words\
    # and then repeat the process above for each of these test words)
    for test in words:
        # Temporary dictionary to contain the counts for the word being tested
        temp_count = {}

        for letter in test:
            if letter in temp_count:
                temp_count[letter] +=1
            else:
                temp_count[letter] = 1
        
        # If the tested word is indeed an anagram of the input word, append it to\
        # the list of matched words, else it is ignored
        if temp_count == word_counts:
            matches.append(test)
    
    print(f'Anagrams found in {words} for "{word}":\n{matches}')
    return matches

print('Solution 2')
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print()

# In reality, I could have just done this
def anagrams(word, words): return [test_word for test_word in words if sorted(word) == sorted(test_word)]

print('One-liner')
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))