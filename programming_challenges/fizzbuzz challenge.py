#FizzBuzz challenge: numbers from 1 to 100; if the number is a multiple of 3 print 'Fizz', if the number is a multiple of 5 print 'Buzz', if the number is a multiple of 3 and 5 print 'FizzBuzz', else print the number

for num in range(1,101): #numbers 1 to 100
    if (num % 3 == 0) and (num % 5 == 0): #if multiple of 3 and 5
        print('FizzBuzz')
    elif num % 3 == 0: #if only a multiple of 3
        print('Fizz')
    elif num % 5 == 0: #if only a multiple of 5
        print('Buzz')
    else: #numbers that aren't either a multiple of 3 or 5
        print(num)