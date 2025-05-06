from collections import deque

arr = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0]
]

#? Space complexity O(n*m)
#? Time complexity: O(n*m)
def numberOfLands(arr: list[list[int]]) -> int:
    total_num_of_lands = 0
    n, m = len(arr), len(arr[0])
    visited = [[0]*m for _ in range(n)]
    q = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #? O(n)
    for row in range(n):
        #? O(m)
        for col in range(m):
            if arr[row][col] == 0 or visited[row][col]: continue
            total_num_of_lands += 1
            q.append((row, col))
            visited[row][col] = 1
            #? O(island_size)
            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
                
            
    return total_num_of_lands
        

print(numberOfLands(arr))