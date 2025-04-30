import random
from collections import defaultdict

arr = [
    'god', 'dog', 'enlist', 'google', 'okl', 'gooegl', 'fuk', 'act', 'goooooood', 'cat', 'silent', 'listen', 'tac']
# random.shuffle(arr)
# print(arr)



def returnAnagramsFromVector(list_of_strings: list[str]) -> list[list[str]]:
    
    def createKey(s: str) -> tuple[int]:
        key = [0]*26
        for letter in s:
            key[ord(letter) - ord('a')] += 1
        return tuple(key)
    
    hashMap = defaultdict(list)

    for string in list_of_strings:
        hashMap[createKey(string)].append(string)
    
    return list(hashMap.values())


print(returnAnagramsFromVector(arr))