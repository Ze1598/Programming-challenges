#codeacademy challenge
#https://discuss.codecademy.com/t/challenge-anagram-detector/83127

string1 = input('Enter the first expression:') #string input 1
string2 = input('Enter the second expression:') #string input 2

#calculate factorial
def result_fact(x):
    fact = 1
    for x in range(x,0,-1):
        fact *= x
    return fact


#this list is used to make sure only letters are counted as characters contained in the inputs
alphabet_caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

string1_letters=[] #list to contain all letters used in string1
string2_letters = [] #list to contain all letters used in string2

#getting all the characters in the first string
for char in string1:
    if char in alphabet: #only letters matter for this
        string1_letters.append(char)

#getting all the characters in the second string
for char in string2:
    if char in alphabet: #only letters matter for this
        string2_letters.append(char)




if sorted(string1_letters) != sorted(string2_letters):
    print('The expressions you entered aren\'t anagrams because the same letters aren\'t used in equal proportion in each expression.')
else: #if the expressions are an anagram
    print('The expressions you\'ve entered are an anagram.')


anagrams_divisor = 1    
used_letters =[]

for char in string1_letters:
    if char not in used_letters:
        used_letters.append(char)
        count = string1.count(char)
        letter_fact = result_fact(count)
        anagrams_divisor *= result_fact(string1.count(char))
       
anagram_dividend = result_fact(len(set(string1_letters)))

print('With the expression you\'ve entered you can create', anagram_dividend / anagrams_divisor,'anagrams.')
    
    



'''
what_to_do = input('What do you want to do? Test the number of possible anagrams to do with 2 expressions or test if 2 expressions are an anagram?')

if 'test' in what_to_do.lower():
    string1 = input('Enter the first expression:') #string input 1
    string2 = input('Enter the second expression:') #string input 2
    anagram(string1,string2)

else:
    x = int(input('Enter a positive integer:'))
'''