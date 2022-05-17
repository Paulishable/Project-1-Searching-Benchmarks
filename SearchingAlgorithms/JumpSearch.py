import math


# Jump Search
def jump_search(an_array, the_target):
    n= len(an_array)
    # Finding block size to be jumped
    step = math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while an_array[int(min(step, n) - 1)] < the_target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while an_array[int(prev)] < the_target:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

    # If element is found
    if an_array[int(prev)] == the_target:
        return prev

    return -1

