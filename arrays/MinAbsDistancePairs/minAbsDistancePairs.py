from math import inf

def minAbsDistancePairs(arr: list[int]) -> list[list[int]]:

    def quicksort(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

    sorted_arr = quicksort(arr)

    results = []
    min_abs_value = inf
    for n1, n2 in zip(sorted_arr[:-1], sorted_arr[1:]):
        abs_value = abs(n1 - n2)
        if abs_value == min_abs_value:
            results += [[n1, n2]]
        elif abs_value < min_abs_value:
            min_abs_value = abs_value
            results = [[n1, n2]]

    return results
