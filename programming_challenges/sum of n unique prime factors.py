#sum of n's unique prime factors
def prime_num():
    n = input("Choose a positive integer greater than 1:")#user input of a single positive integer
    b = int(n) #turning the input into a integer type
    divisor = 2 #starting the divisor variable at 2 because that's the lowest prime factor possible
    prime_factors = [] #list of all the prime factors of n
    pf_sum = 0 #initializing the sum of n's prime factors at 0
    
    if b == 1:
        print()
        print('The number 1 is called a unit. It has no prime factors and is neither prime nor composite.') #output in case user inputs 1
    else:
        while b > 1: #loop to be repeated while b is higher than 1
            if b % divisor == 0: 
                prime_factors.append(divisor) #if b/divisor 's remainder is 0 then divisor will be added to the prime_factors list as a prime factor of n
                b = b / divisor #lower b to the value of b/divisor to make sure the prime factorization doesn't repeat itself
            else:
                divisor += 1 #in case the divisor wasn't a prime factor then we add 1 to the current divisor
    
    '''print(prime_factors) #debugging'''
    
    if int(n) != 1:
        prime_factors = set(prime_factors) #making a new list of prime_factors composed only by unique prime factors of n
        for num in prime_factors: #a loop to execute the sum of all of n's unique prime factors
            pf_sum += num
        print()
        print('{}\'s prime factors are {} and its unique prime factors\' sum is {}.'.format(n, prime_factors, pf_sum)) #final output

