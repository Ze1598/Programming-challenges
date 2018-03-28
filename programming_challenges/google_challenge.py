#https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string#!
'''Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.
Note: D can appear in any format (list, hash table, prefix tree, etc.
For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"
The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.'''
import collections

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

def find_longest_word_in_string(letters, words):
    #Create a defaultdict, initialized with a list
    letter_positions = collections.defaultdict(list)
    #Loop through the letters in 'S', to obtain each letter and the indexes it appears at
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    print(letter_positions)
    #Loop though the sorted set of words, in descending order of word length
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        #The index of the character we are currently testing
        pos = 0
        #Loop through the letters of the current 'word'
        for letter in word:
            #If 'letter' is not present in 'letter_positions' then it is not present in 'S', so just move on to the next word
            if letter not in letter_positions:
                break
            #Get a list of all the possible positions for the current letter; the positions are only possible if the position is not lower than the current 'pos'ition
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            #If 'possible_positions' is empty it means there were no possible positions, so move on to the next word
            if not possible_positions:
                break
            #The current position is now the first value in 'possible_positions' plus 1; in cases when this is the last time the letter appears, we'd stay forever at the same position, but by adding 1 we will always move on at least to the next position
            pos = possible_positions[0] + 1
        #If we reach this else, then it means this is the longest word from 'D' that appears in 'S', so simply return that word
        else:
            return word
print("able")
print(find_longest_word_in_string(S,D))