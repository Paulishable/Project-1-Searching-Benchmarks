import random
import math
from time import perf_counter


# Linear Search
def jump_search(a_lyst, target):
    # Finding block size to be jumped
    n = len(a_lyst)
    step = math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while a_lyst[int(min(step, n) - 1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return False

    # Doing a linear search for x in
    # block beginning with prev.
    while a_lyst[int(prev)] < target:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return False

    # If element is found
    if a_lyst[int(prev)] == target:
        return True

    return False


# Linear Search
def linear_search(a_lyst, target):
    # Going through array sequentially
    n = len(a_lyst)
    for i in range(0, n):
        if a_lyst[i] == target:
            return True
    return False


# Binary Search
def binary_search(a_lyst, target):
    low = 0
    high = len(a_lyst) - 1
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if a_lyst[mid] == target:
            return True

        elif a_lyst[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return False


# Create a list of Random Numbers...

random.seed(123987)
num = 60
random_list = random.sample(range(10000000), k=num)
# print(random_list)

lyst = sorted(random_list)

# print(lyst)
x_min = lyst[0]
x_max = lyst[-1]
x_mid = lyst[num // 2]
x_not_present = -1

n = 3
m = 4
timing_results = [[0] * m for i in range(n)]


def do_the_searches(the_target, test_id):
    linear_search_start = perf_counter()
    result = linear_search(lyst, the_target)
    linear_search_end = perf_counter()

    linear_search_time = linear_search_end - linear_search_start
    timing_results[0][test_id] = linear_search_time

    binary_search_start = perf_counter()
    result = binary_search(lyst, the_target)
    binary_search_end = perf_counter()

    binary_search_time = binary_search_end - binary_search_start
    timing_results[1][test_id] = binary_search_time

    jump_search_start = perf_counter()
    result = jump_search(lyst, the_target)
    jump_search_end = perf_counter()

    jump_search_time = jump_search_end - jump_search_start
    timing_results[2][test_id] = jump_search_time


the_target = x_min
do_the_searches(the_target, 0)

the_target = x_mid
do_the_searches(the_target, 1)

the_target = x_max
do_the_searches(the_target, 2)

the_target = x_not_present
do_the_searches(the_target, 3)

print(f"\n  ALGORITHM    First Element   Middle Element   Last Element   Not an element")
print("Linear Search", "    %.3e" % timing_results[0][0], "      %.3e" % timing_results[0][1],
      "      %.3e" % timing_results[0][2], "     %.3e" % timing_results[0][3])
print("Binary Search", "    %.3e" % timing_results[1][0], "      %.3e" % timing_results[1][1],
      "      %.3e" % timing_results[1][2], "     %.3e" % timing_results[1][3])
print("  Jump Search", "    %.3e" % timing_results[2][0], "      %.3e" % timing_results[2][1],
      "      %.3e" % timing_results[2][2], "     %.3e" % timing_results[2][3])
