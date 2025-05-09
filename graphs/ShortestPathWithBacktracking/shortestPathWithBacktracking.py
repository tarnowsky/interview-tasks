from collections import deque
from pprint import pprint
from typing import List, Optional

deMap = [[j+10*i for j in range(10)] for i in range(10)]
target = 15

def shortestPathWithBacktracking(arr: List[List[int]], target: int) -> Optional[List[int]]:
    n, m = len(arr), len(arr[0])
    visited = [[False]*m for _ in range(n)]
    parent = [[None]*m for _ in range(n)]

    q = deque([(0, 0)])
    visited[0][0] = True

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            rn, cn = r + dr, c + dc
            if 0 <= rn < n and 0 <= cn < m and not visited[rn][cn]:
                visited[rn][cn] = True
                parent[rn][cn] = (r, c)
                if arr[rn][cn] == target:
                    # Backtracking
                    path = []
                    cr, cc = rn, cn
                    while (cr, cc) != (0, 0):
                        path.append(arr[cr][cc])
                        cr, cc = parent[cr][cc]
                    path.append(arr[cr][cc])
                    path.reverse()
                    return path
                q.append((rn, cn))
    return None


pprint(deMap)
print(target)
print(shortestPathWithBacktracking(deMap, target))


