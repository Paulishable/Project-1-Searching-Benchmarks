# Linear Search
def linear_search(an_array, target):
    # Going through array sequentially
    n = len(an_array)
    for i in range(0, n):
        if an_array[i] == target:
            return i
    return -1
