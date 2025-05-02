## Task Description
Given string s, return the longest palindromic substring in s

---

### Solution
Dynamic solution. We build 2d matrix db and then use i and j.  
```
dp[i][j] = isPalindrom(s[i:j+1])
```

#### Start:
1. ```dp[x][x] = True```
2. ```if s[i] == s[i+1]: dp[x][x+1] = True```
#### Algo

```if j > i + 1: ```  
```dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]```

when ```dp[i][j] == True``` we check the longest palindrom which is ```j - i + 1``` and by saving the ```i``` also we can return the palindrom which will be ```s[start:start+longest_palindrom]```

### Constraints and Complexity
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(n^2)