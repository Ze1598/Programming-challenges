# https://discuss.codecademy.com/t/challenge-prime-number-printer/101926
# Write a function, primeNumberPrinter, that will print out all prime numbers in a given string.
# Function Name: primeNumberPrinter
# Input: A single string
# Output: An integer array of the prime numbers contained in the string
# Example: primeNumberPrinter("abc2134kd31"), will output an array [2,13,3,3,31] (in the order they appear in the string).

# receive a string as input; this string can contain all sorts of characters, it only if matters if a character is a digit or not 
# from the string obtain only the digits contained in it, and non-digit characters turn into dots (.)
# then get all the possible numbers contained in that string; add digit by digit to the variable number; if a dot is between digits then the current number stops there, is added to the list numbers_list, and the variable number is reset to an empty string ''
# after this test each number (n) contained in numbers_list; if the n is a prime number then append it to num_output; else ignore n 
# lastly, output the results

# note: in this case in particular i only checked for 3-digits or less numbers

string1 = 'abc2134kd31'
string2 = 'ede25jnbh73'


def primeNumberPrinter(string): 
    num_output = [] #list to contain all prime numbers from the initial string
    clean_string = '' #string to contain the input string without non-digit characters
    
    for char in string: #loop to form clean_string
        if char.isdigit() == True: #if char is a digit add it to clean_string
            clean_string += char
        else: #if char isn't a digit add a '.' instead to clean_string
            clean_string += '.'

    numbers_list = [] #list to hold all the possible numbers; can include repeated numbers
    number = '' #variable to hold the current number being dealt with
    i = 0 #index
    
    for char in clean_string: #loop through clean_string
        if char != '.': #if char is a digit
            number += char #add char to number; currently number is a 1 digit number
            numbers_list.append(int(number)) #add number to the list containing all numbers
            if clean_string.index(char) > (len(clean_string)-1): #test if this char is the last char of clean_string
                break #if it is terminate the loop
            
            if (i+1) > (len(clean_string)-1): #test if this index would be out of range
                pass #if it is ignore it
            elif clean_string[i + 1] == '.':
                number = '' #if char isn't a digit then it means the digit chain was broken; reset number variable
            else:
                digit2 = clean_string[i+1] #else add to number the next digit in clean_string
                number += digit2 #number is currently a 2-digit number
                numbers_list.append(int(number)) #add number to the list containing all numbers
            
            
            if (i+2) > (len(clean_string)-1): #test if this index would be out of range
                number = '' #if it is, just reset number to an empty string and proceed to the next looping sequence
                pass
            elif clean_string[i+2] == '.':
                number = ''#if char isn't a digit then it means the digit chain was broken; reset number variable
            else:
                digit3 = clean_string[i+2] #else add to number the second-nex digit in clean_string
                number += digit3 #number is currently a 3-digit number
                numbers_list.append(int(number)) #add number to the list containing all numbers
                number = '' #in this case i only want numbers with max. 3 digits; so it is time to reset number to an empty string
    
        
        i += 1 #before starting the next looping sequence increment i by 1 '''

    #Check for prime numbers from the list containing all numbers present in the string
    for n in numbers_list:
        if n == 1: #if n == 1 then ignore it
            pass
        else: 
            for num in range(2, int(n**(1/2) + 1)): #loop through all the numbers relevant to test if n is a composite
                #as pointed out by @factoradic https://discuss.codecademy.com/t/notes-regarding-your-submission/106631/2
                if n%num == 0: #if at least one num is evenly divisible by n then it means n is not a prime number 
                    break
            else: #if the previous for loop terminated normally then it means n isn't a composite, it's a prime
                num_output.append(n)
    
    #Final Output 
    print('The string {} contains the following prime numbers {}.'.format(repr(string),num_output))
    

primeNumberPrinter(string1)
primeNumberPrinter(string2)