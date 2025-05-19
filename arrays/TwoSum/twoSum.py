from typing import List

def twoSum(arr: List[int], target: int) -> List[int]:
    arr.sort()
    l, r = 0, 1
    while l < r < len(arr):
        csum = arr[l] + arr[r]
        if csum == target: return [l, r]
        if csum > target: l += 1
        else: r += 1

print(twoSum([7, 11, 2, 5], 9))
