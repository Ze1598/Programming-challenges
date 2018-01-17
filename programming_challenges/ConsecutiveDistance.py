# https://www.reddit.com/r/dailyprogrammer/comments/759fha/20171009_challenge_335_easy_consecutive_distance/
# You'll be given two integers 'a' and 'b' on the first line denoting the number of sequences that follow and the length of those sequences, respectively. You'll then be given 'a' integer sequences of length 'b', one per line. The integers will always be unique and range from 1 to 100 inclusive.

def ConsecutiveDistance(a, b, *seq,distance=1):
    pairs_used = []
    num1 = 0
    num2 = 0
    #the total distance of the current sequence
    distance_sum = 0
    #distances from each sequence
    distances = []
    for i in seq:
        # print(i)
        for i2 in i:
            #if 'i2+distance' is in the list, get its distance from 'i2' if the pair hasn't been used yet
            if i2+distance in i:
                num1,num2 = i2, i2+distance
                if {num1,num2} not in pairs_used:
                    distance_sum += abs(i.index(i2) - i.index(i2+distance))
                    pairs_used.append({num1, num2})
            #elif 'i2-distance' is in the list, get its distance from 'i2' if the pair hasn't been used yet
            elif i2-distance in i:
                num1,num2 = i2, i2-distance
                if {num1,num2} not in pairs_used:
                    distance_sum += abs(i.index(i2) - i.index(i2-distance))
                    pairs_used.append({num1, num2})
        #reset 'pairs_used' and 'distance_sum', also append the current 'distance_sum' to 'distances'
        pairs_used = []
        distances.append(distance_sum)
        distance_sum = 0
    for i in distances:
        print(i)
    # return distances
                    

seqs1 = [list((31, 63, 53, 56, 96, 62, 73, 25, 54, 55, 64)), 
    list((77, 39, 35, 38, 41, 42, 76, 73, 40, 31, 10)), 
    list((30, 63, 57, 87, 37, 31, 58, 83, 34, 76, 38)), 
    list((18, 62, 55, 92, 88, 57, 90, 10, 11, 96, 12)), 
    list((26, 8, 7, 25, 52, 17, 45, 64, 11, 35, 12)), 
    list((89, 57, 21, 55, 56, 81, 54, 100, 22, 62, 50))
]
ConsecutiveDistance(6, 11, *seqs1, distance=1)
print()

seqs2 = [
    list((76, 74, 45, 48, 13, 75, 16, 14, 79, 58, 78, 82, 46, 89, 81, 88, 27, 64, 21, 63)),
    list((37, 35, 88, 57, 55, 29, 96, 11, 25, 42, 24, 81, 82, 58, 15, 2, 3, 41, 43, 36)),
    list((54, 64, 52, 39, 36, 98, 32, 87, 95, 12, 40, 79, 41, 13, 53, 35, 48, 42, 33, 75)),
    list((21, 87, 89, 26, 85, 59, 54, 2, 24, 25, 41, 46, 88, 60, 63, 23, 91, 62, 61, 6)),
    list((94, 66, 18, 57, 58, 54, 93, 53, 19, 16, 55, 22, 51, 8, 67, 20, 17, 56, 21, 59)),
    list((6, 19, 45, 46, 7, 70, 36, 2, 56, 47, 33, 75, 94, 50, 34, 35, 73, 72, 39, 5))
]
ConsecutiveDistance(6, 20, *seqs2, distance=1)