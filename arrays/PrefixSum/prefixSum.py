arr = [5, 2, 9, 1, 3]

def prefixSum(arr: list[int]) -> list[int]:
    result = [arr[0]] if len(arr) > 0 else []
    for i in range(1, len(arr)):
        result.append(result[i-1] + arr[i])
    return result

print(prefixSum(arr))
