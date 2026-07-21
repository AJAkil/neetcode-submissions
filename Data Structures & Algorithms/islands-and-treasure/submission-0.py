from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        Q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
    
        def get_nei(node):
            delta_rows = [-1, 0, 1, 0]
            delta_cols = [0, 1, 0, -1]
            r,c = node 
            res = []

            for i in range(len(delta_rows)):
                nei_r = r + delta_rows[i]
                nei_c = c + delta_cols[i]

                if 0 <= nei_r < ROWS and 0 <= nei_c < COLS and grid[nei_r][nei_c]==INF:
                    res.append((nei_r, nei_c))
            return res
    
        # fill in with the sources
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    Q.append((i,j))

        dist = 0
        while len(Q) > 0:
            n = len(Q)
            for _ in range(n):
                node = Q.popleft()
                grid[node[0]][node[1]] = dist
                for nei in get_nei(node):
                    # check if already visited
                    if nei in visited:
                        continue
                    
                    Q.append(nei)
                    visited.add(nei)
                    
            dist += 1

        