# codecademy challenge may 4th
# https://discuss.codecademy.com/t/challenge-reverse-words/83796

# this program splits an expression word by word and reverses it, keeping the original index of any symbols the same
def rev_input(string):
    
    string += ' ' #i add a space at the end of the expression because if i don't later when looping to get each word in the expression it won't add the last word

    alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    alphabet_caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    

    temp_word = '' #variable to hold words in the loop
    word_list = [] #list to contain all the words in the input
    
    symbols_index =[] #index of any symbols in the expression
    
    for char in string: #loop to get the index of any symbols 
        if (char not in alphabet_caps) and (char not in alphabet) and char != ' ':
            symbols_index.append(string.index(char))
    

    for i in string: #loop through the expression to get all the words in it 
        if i == ' ': #if the character is a space then it means it's the end of a word; add that word to the list containing the words, and then add the space as another item
            word_list.append(temp_word)
            word_list.append(i)
            temp_word = ''
        elif (i not in alphabet_caps) and (i not in alphabet): #if the character is not a space or a letter the loop ignores it
            pass
        else: #if the character is a letter than we add it to the temp_word variable meaning the current word isn't complete yet
            temp_word += i

    char_list = [] #list to contain every single character from the expression including spaces in reversed order; this will help inserting the symbols in the correct index
    
    for char in word_list[::-1]: #looping through each word in the expression, in reversed order
        for char2 in char:
            if char_list != '':
                char_list.append(char2) #char_list gets every single character in the expression in reversed order; excluding the symbols
                
    char_list.remove(' ') #this removes the space added in the beginning of the script

    for i in symbols_index: #now that i have the reversed order of each character of the expression i can simply insert the symbols in the correct index
        char_list.insert(i,string[i])

    rev_exp = '' #variable to hold the final result
    for char in char_list: #loop to do just that
        rev_exp += char
    
    return rev_exp #return the final result so it's possible to print outside the script

print(rev_input('outlast is sh!t'))
print(rev_input('May the Fourth be with you'))
print(rev_input('Persona is amazing!'))