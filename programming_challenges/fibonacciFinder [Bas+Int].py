#Basic difficulty
#simply execute the Fibbonnaci Sequence until the 50th number is found

def fibonacciFinder50():
    fibonacci_number = 2 #this variable will show the place of the current fibonacci_number in the sequence of results; in this case what matter is when this variable reaches 50; it starts at 2 because we already know the 1st and 2nd numbers of the sequence: 0 and 1
    
    a = 0 #first value of the sequence 
    b = 1 #second value of the sequence
    c = b #holds the value of b
    
    while fibonacci_number != 50:
        fibonacci_number += 1 #increment the count along with getting the next fibonacci number
        b += a #b just gets added the current value of a
        a = c #a becomes the previous value of b; which is held in c
        c = b #now "reset" c to the current value of b
    else:
        return b #in this case it returns the 50th number in the Fibbonnaci Sequence
    
print('fibonacciFinder50() =>', fibonacciFinder50())

#Intermediate difficulty
#basically the same as basic difficulty, except the sequence is executed until the nth number is found, in this example it's the 300th number 

def fibonacciFinderN(n):
    fibonacci_number = 2 #this variable will show the place of the current fibonacci_number in the sequence of results; in this case what matter is when this variable reaches 50; it starts at 2 because we already know the 1st and 2nd numbers of the sequence: 0 and 1
    
    a = 0 #first value of the sequence 
    b = 1 #second value of the sequence
    c = b #holds the value of b
    
    if n < 1: #if n is lower than 1 prompt the user for another n until n is 1 or higer
        while n < 1:
            n = int(input('That\'s not a valid number. Choose a number higher than 1. '))
    if n == 1:
        return a
    elif n == 2:
        return b 
    else:
        while fibonacci_number != n:
            fibonacci_number += 1 #increment the count along with getting the next fibonacci number
            b += a #b just gets added the current value of a
            a = c #a becomes the previous value of b; which is held in c
            c = b #now "reset" c to the current value of b
        else:
            return b #in this case it returns the 50th number in the Fibbonnaci Sequence
    
print('fibonacciFinderN(300) =>', fibonacciFinderN(300))