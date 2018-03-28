#Take a binary number as input and count the maximum number of consecutive '1's (bits turned on)

def count_ones(x):
    #Current count of consecutive 1s found
    counter = 0
    #List to hold all the 'counter' values
    counts = []
    #Loop through the binary number, but only starting in the 3rd character (excludes '0b')
    for i in range(2,len(x)):
        #If the character is '1' then increment the current count by 1
        if x[i] == '1': counter += 1
        #Else, if counter is not 0 then append it to 'counts' and reset 'counter'; always reset 'counter'
        else:
            if counter != 0: counts.append(counter)
            counter = 0
    #Append the last value held by 'counter' when it exited the loop
    counts.append(counter)
    return max(counts)

n = bin(5)
m = bin(13)
o = bin(1000)
p = bin(439)

print(int(n,2), n, count_ones(n))
print(int(m,2), m, count_ones(m))
print(int(o,2), o, count_ones(o))
print(int(p,2), p, count_ones(p))