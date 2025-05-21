from typing import List, Tuple
from collections import deque
from pprint import pp

arr = [
    [1, 1, 2, 2, 3],
    [1, 1, 2, 3, 3],
    [4, 4, 2, 3, 3],
    [4, 4, 4, 3, 3],
    [5, 5, 4, 4, 3]
]

def floodFillPaint(
    screen: List[List[int]],
    location: Tuple[int,int],
    color: int,
    ) -> List[int]:
    
    n, m = len(screen), len(screen[0])
    visited = [[False]*m for _ in range(n)]
    row, col = location
    curr_color = screen[row][col]

    dest = [(0, 1), (0, -1), (1,0), (-1, 0)]
    q = deque()
    q.append((row, col))

    while q:
        row, col = q.popleft()
        if screen[row][col] == curr_color:
            visited[row][col] = True
            screen[row][col] = color
            for dr, dc in dest: 
                nr = row + dr
                nc = col + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    q.append((nr, nc))
    
    return screen


pp(floodFillPaint(arr, (0, 4), 8))


