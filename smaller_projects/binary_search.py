# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!

import random
import time

# naive search:
# scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1


def naive_search(l, target):
    # l = sorted(l)
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def naive_search_b(l, target):
    # using just i puts the value of i, and the corresponding value in a tupple
    # using i and j, creates individual values for both
    # l = sorted(l)
    for i, j in enumerate(l):
        if j == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our klist is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # example list = [1, 3, 5, 10, 12] | should return 3 the index of 10
    # l = sorted(l)
    mid_point = (low + high) // 2

    if l[mid_point] == target:
        return mid_point
    elif l[mid_point] > target:
        return (binary_search(l, target, low, mid_point-1))
    else:
        # l[mid_point] < target
        return binary_search(l, target, mid_point+1, high)


if __name__ == "__main__":

    # l = [1, 3, 5, 10, 12]
    # target = 10

    # print(f"Naive search function produced: {naive_search(l, target)}")
    # print(f"Naive search function b produced: {naive_search_b(l, target)}")
    # print(f"Binary search produced: {binary_search(l, target)}")

    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f"Naive search time: {(end - start/length)} seconds")

    start = time.time()
    for target in sorted_list:
        naive_search_b(sorted_list, target)
    end = time.time()
    print(f"Naive search b time: {(end - start/length)} seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f"Binary search time: {(end - start)/length} seconds")
