def findLongestSubHolidaySubArray(arr: list[str], num_of_off_days: int) -> int:
    n = len(arr)
    left = 0
    holidays_spent = 0
    result = 0
    for right in range(n):
        if arr[right] == 'w':
            holidays_spent += 1
        while holidays_spent > num_of_off_days:
            if arr[left] == 'w':
                holidays_spent -= 1
            left += 1
        
        result = max(result, (right - left + 1))
    return result




arr = ['w', 'h', 'w', 'h', 'h', 'w', 'w', 'h', 'h', 'w']
days_off = 2

print(findLongestSubHolidaySubArray(arr, days_off))