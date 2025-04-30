from pprint import pprint
string = "aadlkakdjkljdallkjduikkajakkzmnbckjvxlytqhwgvakkkkcnadoiczuy"

def longestPalindormSubstring(s: str) -> str:
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    curr_max_len = 0
    start = 0
    for i in range(n, -1, -1):
        for j in range(i, n):
            if j == i: 
                dp[i][j] = True
            elif j == i + 1: 
                dp[i][j] = s[i] == s[j]
            elif j > i + 1:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            
            if dp[i][j]:
                if (j - i + 1) > curr_max_len:
                    start = i
                    curr_max_len = (j - i + 1)
    return s[start:(start + curr_max_len)]

print(longestPalindormSubstring(string))