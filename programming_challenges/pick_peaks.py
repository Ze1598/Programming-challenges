# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/solutions/python
# Write a function that returns the positions and the values of the\
# "peaks" (or local maxima) of a numeric array.
# https://en.wikipedia.org/wiki/Maxima_and_minima

def pick_peaks(arr):
    # List of the indexes (positions) for the peak values
    pos = []
    # Loop through the input array, but never test both the first and last values
    for i in range(1, len(arr)-1):
        # If the current value is bigger than the previous one
        if arr[i-1] < arr[i]:
            # And it also bigger than the next one or equal to it and different than\
            # the last one (the last one part is to prevent plateaus that extend\
            # until the end of the array)
            if arr[i] > arr[i+1] or (arr[i] == arr[i+1] and arr[i] != arr[-1]):
                pos.append(i)

    # In short, look for values that are bigger than the previous and next values or\
    # just the first value of a plateau, as long as that plateau doesn't last until\
    # the end of the array

    return {"pos":pos, "peaks":[arr[i] for i in pos]}
    
    
print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))
print({"pos":[3,7], "peaks":[6,3]})
print()
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))
print({"pos":[3,7], "peaks":[6,3]})
print()
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
print({"pos":[3,7,10], "peaks":[6,3,2]})
print()
print(pick_peaks([2,1,3,1,2,2,2,2]))
print({'pos': [2], 'peaks': [3]})
print()
# Unfortunately, seems like the function picks up the first value of\
# 2-values peaks as a peak, and it shouldn't
print(pick_peaks([17, 12, 14, 8, 5, 10, 1, 5, 16, 16, 19, 6, -3, 8, 13]))
print({'pos': [2, 5, 10], 'peaks': [14, 10, 19]})
print()
print(pick_peaks([11, 1, 3, 4, -4, 7, 5, 4, 0, 4, 12, 3, 11, -2, 10, 5, 0, 11, 11, 17, -4, 1, 3, -3, 20, -4, 4, 4, 4]))
print({'pos': [3, 5, 10, 12, 14, 19, 22, 24], 'peaks': [4, 7, 12, 11, 10, 17, 3, 20]})