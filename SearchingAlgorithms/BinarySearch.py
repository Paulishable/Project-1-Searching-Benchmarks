# Binary Search
def binary_search(an_array, target):
    low = 0
    high = len(an_array) - 1
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if an_array[mid] == target:
            return mid

        elif an_array[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1
