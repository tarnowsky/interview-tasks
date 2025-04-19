from collections import defaultdict, deque

words = ["baa", "abcd", "abca", "cab", "cad"]

def findOrder(words: list[str]) -> list[str]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_letters = set()

    for word in words:
        for letter in word:
            all_letters.add(letter)

    for word1, word2 in zip(words[:-1], words[1:]):
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                u, v = word1[i], word2[i]
                graph[u].append(v)
                in_degree[v] += 1
                break
    
    queue = deque()
    for letter in all_letters:
        if in_degree[letter] == 0:
            queue.append(letter)
    
    result = []
    while queue:
        letter = queue.popleft()
        result.append(letter)
        for neighbor in graph[letter]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result    

print(findOrder(words=words))
                

    