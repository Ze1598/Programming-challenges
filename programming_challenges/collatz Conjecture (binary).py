# https://en.wikipedia.org/wiki/Collatz_conjecture
# https://stackoverflow.com/questions/25106002/python-adding-binary-number

# The machine will perform the following three steps on any odd number until only one "1" remains:
# Append 1 to the (right) end of the number in binary (giving 2n + 1);
# Add this to the original number by binary addition (giving 2n + 1 + n = 3n + 1);
# Remove all trailing "0"s (i.e. repeatedly divide by two until the result is odd).
'''
print(0b111) #7
print(0b1111) #15
print(0b10110) #22
print(0b1011) #11
print(0b10111) #23
print(0b100010) #34
print(0b10001) #17
print(0b100011) #35
print(0b110100) #52
print(0b1101) #13
print(0b11011) #27
print(0b101000) #40
print(0b101) #5
print(0b1011) #11
print(0b10000) #16
print(0b1) #1
print(0b11) #3
print(0b100) #4
print(0b1) #1
print()
print()
'''
'''
a = '7'
b = '1'
print(int(a)+int(b))
c = '7'
d = 1
print(bin(int(c)+d))
# e = format(0b111,'b')
# print(e)
# print(type(e))
# z = 7
# print(type(str(bin(z))+'1'))
# print(type(z))
# print(z)
'''
'''
#append a 1 to the end of a binary number
print('-',0b111 | 0b0001)
    #shift every bit in the number 1 unit to the left, which means the last bit is now zero(false), then use a bit mask to turn that last bit true, which effectively appends 1 to a binary number
print('--',bin(0b111<<1 | 0b00001))
print()
#way to remove a trailing zero, one zero at a time
a = 0b10
print('---',a >> 1)
'''
#this function calculates the collatz conjecture sequence for a number n; this version deals with the numbers as integers
def collatz(n):
    #this will be the number that suffers the opperations (append 1 and remove trailing zeros)
    n_ = n
    n__ = n_
    #counts how many loops were needed to complete the conjecture
    count = 0
    #simply holds the sequence of numbers that have been calculated, with 'n' being the first number in the sequence
    sequence = [n]
#repeat the loop until the number has been reduced to 1 (0b1)
    while n_ != 1:
        # print('count', count)
        # print('n',n)
        # print('n_ begin loop',bin(n_))
#append 1 to the current binary number
        #shift every bit in 'n_' one bit to the left so that that the last bit will now be 0/false/turned off; then using Or (|) and a bit mask (0b1) turn on that that bit
        n_ = n_ << 1 | 0b1
        sequence.append(n_)
#add the current binary number to the original number 'n'
        # print('n_ after append',bin(n_),n_)
        n_ += n__
        sequence.append(n_)
#remove trailing zeros (divide by two until the number is odd aka ends in 1)
        # print('n_ after sum', bin(n_),n_)
        # print('str', str(bin(n_))[::-1][0])
        while bin(n_)[::-1][0] == '0':
            n_ = n_ >> 1
        # print('n_ after trail', bin(n_),n_)
        sequence.append(n_)
        #after removing trailing zeros store a copy of it in 'n__', so after we append 1 to 'n_' we can add it to the previous number in the sequence
        n__ = n_
        # if count == 3:
        #     break
        count += 1
        # print('count', count, 'n_',n_)
        # print()
    print(sequence)
    return count

#this function works the same way as 'collatz' but only deals with the numbers in binary form and operates with them as strings
def collatz2(n):
    n = bin(n)
    n_ = n
    n__ = n
    sequence = [n]
    count = 0 
#repeat the loop until the number has been reduced to 1 (0b1)
    while n_ != '0b1':
        # print('count',count)
#append 1 to the current binary number
        n_ += '1'
        sequence.append(n_)
        # print('n_ after append', n_,int(n_,2), type(n_))
#add the current binary number to the original number 'n'
        n_ = bin(int(n_,2) + int(n__,2))
        sequence.append(n_)
        # print('n_ after add', n_,int(n_,2), type(n_))
#remove trailing zeros (divide by two until the number is odd aka ends in 1)        
        while n_[::-1][0] == '0':
            n_ = n_[:len(n_)-1]
        # print('n_ after trail',n_,int(n_,2), type(n_))
        #after removing trailing zeros store a copy of it in 'n__', so after we append 1 to 'n_' we can add it to the previous number in the sequence
        n__ = n_
        sequence.append(n_)
        count += 1
        # print()
    print(sequence)
    return count

print('collatz(7) =>',collatz(7))
print()
print('collatz(3) =>',collatz(3))
print()
print('collatz2(7) =>',collatz2(7))
print()
print('collatz2(3) =>', collatz2(3))
print()
print('collatz2(1) =>', collatz2(1))