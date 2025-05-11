import unittest
from collections import defaultdict

class Tests(unittest.TestCase):
    def testClassic(self):
        self.assertEqual(
            longestSubstringNoRepeatingChars('siemas'),
            'siema'
        )
        self.assertEqual(
            longestSubstringNoRepeatingChars('ssssiemas'),
            'siema'
        )
        self.assertEqual(
            longestSubstringNoRepeatingChars('siemasieman'),
            'sieman'
        )
        self.assertEqual(
            longestSubstringNoRepeatingChars('abcabcbb'),
            'abc'
        )
        self.assertEqual(
            longestSubstringNoRepeatingChars('bbbbb'),
            'b'
        )
        self.assertEqual(
            longestSubstringNoRepeatingChars('pwwkew'),
            'wke'
        )
    

def longestSubstringNoRepeatingChars(s: str) -> str:
    result = ''
    curr_length = 0
    max_length = 0
    d = defaultdict(int)
    l = 0
    for r in range(len(s)):
        c = s[r]
        d[c] += 1
        if d[c] < 2:
            curr_length += 1
            if curr_length > max_length:
                result = s[l:r+1]
        
        while d[c] > 1 and l <= r:
            if s[l] == c:
                d[c] -= 1
                l+=1
                break
            d[s[l]] = 0
            l+=1

    return result

def longestSubstringNoRepeatingCharsGPT(s: str) -> str:
    char_index = {}
    l = 0
    max_len = 0
    start = 0

    for r, c in enumerate(s):
        if c in char_index and char_index[c] >= l:
            l = char_index[c] + 1
        char_index[c] = r
        if r - l + 1 > max_len:
            max_len = r - l + 1
            start = l

    return s[start:start + max_len]
        


if __name__ == '__main__':
    unittest.main()