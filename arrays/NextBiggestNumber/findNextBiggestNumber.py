from math import inf

arr = [
    23, 45, 12, 67, 89, 34, 56, 78, 90, 11,
    22, 33, 44, 55, 66, 77, 88, 99, 10, 25
]

def nextBiggestNumber(arr: list[int], num: int) -> int:
    nextBiggest = inf
    for n in arr:
        if n < nextBiggest and n > num:
            nextBiggest = n
    return nextBiggest if nextBiggest < inf else -1

print(nextBiggestNumber(arr, 99))
        
    