# https://discuss.codecademy.com/t/challenge-palindrome-detector/140137
# Write a function, isPermPalindrome, that will test if a given string is a permutation of a palindrome.
# Function Name: isPermPalindrome
# Input: a String consisting only of lowercase letter characters
# Output: a boolean, true if the string is a permutation of a palindrome and false if the string is not a permutation of a palindrome
# Examples:
# isPermPalindrome("kayak") => true
# isPermPalindrome("yakak") => true

#this comment helped me with the logic for the script: https://stackoverflow.com/a/31224782/7601147

#receive a string and count how many times each unique letter appears
#if all letters have an even number of appearances then String is a permutation of a palindrome
#else if there's only one letter that appears an odd number of times, String is still a permutation of a palindrome
#if there's more than one letter with an odd number of appearances then String is not a permutation of a palindrome

# [Basic difficulty]
# imports
from collections import Counter
'''
def isPermPalindrome(String):
    letter_counter = list(Counter(String).values()) #this gets me a list containg how many times each letter appears in String
    odd_count = 0 #this will count how many unique letters in string appear a odd number of times
    
    for num in letter_counter:
        if num%2 == 0:
            pass
        else:
            odd_count += 1
    
    return bool(odd_count <= 1)
    

print('isPermPalindrome("kayak") =>', isPermPalindrome('kayak'))
print('isPermPalindrome("yakak") =>', isPermPalindrome('yakak'))
print('isPermPalindrome("anna") =>', isPermPalindrome('anna'))
print('isPermPalindrome("civic") =>', isPermPalindrome('civic'))
print('isPermPalindrome("level") =>', isPermPalindrome('level'))
'''
#[Intermediate difficulty]
# As above, but isPermPalindrome should now be able to account for punctuation, spaces, and capitalization in the input string.
# Your input string may now include spaces, numbers, punctuation, and capitalization, but in assessing whether the string is a palindrome or not, spaces, punctuation, and capitalization does not matter. For example, akyKa is a permutation of Kayak, but we don't care that there is one upper case K and one lower case k in Kayak – this is still a palindrome.
# Example: isPermPalindrome("Science Bros.") => false

def isPermPalindrome_int(String):
    strippred_String = '' #will hold String filtered of spaces, punctuation and capitalized letters
    for char in String.lower(): #this gets rid of capitalized letters right off the bat
        # print('char =>',char)
        if char == ' ': #ignore spaces
            pass
        elif char.isalnum() == False: #if char is not a letter or a digit ignore it
            pass
        else: #if char is a letter or a digit then add it to strippred_String
            strippred_String += char
    # print('strippred_String =>', strippred_String)
    letter_counter = list(Counter(strippred_String).values()) #creates a list containg how many times each letter appears in String
    
    odd_count = 0 #this will count how many unique letters in string appear a odd number of times
    
    for num in letter_counter: #now use this loop to check how many unique letters have an odd number of appearances
        if num%2 == 0:
            pass
        else:
            odd_count += 1
    
    #if there's more than one unique letter that appears an odd number of times in String return False; else return True
    return bool(odd_count <= 1)


print('isPermPalindrome_int("kayak") =>', isPermPalindrome_int('kayak'))
print('isPermPalindrome_int("yakak") =>', isPermPalindrome_int('yakak'))
print('isPermPalindrome_int("Science Bros.") =>', isPermPalindrome_int('Science Bros.'))
print('isPermPalindrome_int("121") =>', isPermPalindrome_int('121'))
print('isPermPalindrome_int("Don\'t nod.") =>', isPermPalindrome_int('Don\'t nod.'))
print('isPermPalindrome_int("I did, did I?") =>', isPermPalindrome_int('I did, did I?'))
print('isPermPalindrome_int("Tpo spot") =>', isPermPalindrome_int('Tpo spot'))
print('isPermPalindrome_int("Was ti a cat I saw?") =>', isPermPalindrome_int('Was ti a cat I saw?'))
print('isPermPalindrome_int("Eva, can I ese bees in a cave?") =>', isPermPalindrome_int('Eva, can I ese bees in a cave?'))
