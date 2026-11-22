class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
        ROWS = len(grid)
        COLS = len(grid[0])

        Q = deque()
        visited = set()
        m = grid
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        # We set the distance matrix
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    m[r][c] = 0
                    Q.append((r,c))
                    visited.add((r,c))
                else:
                    m[r][c] = -1 # we need to use this to update this distance


        # this is for setting up the distance matrix
        while Q:
            n = len(Q)
            for _ in range(n):
                r,c = Q.popleft()
                
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or m[row][col]!= -1 or (row, col) in visited:
                        continue

                    # else we can measure and mark them
                    m[row][col] = m[r][c] + 1 # just 1 step away from the thieves
                    visited.add((row,col))
                    Q.append((row,col))



        def feasible(mid):
            q = deque()
            v = set()

            q.append((0,0))
            v.add((0,0))

            while q:
                # regular BFS, I guess
                r,c = q.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return True
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or m[row][col] < mid or (row, col) in v:
                        continue
                    
                    v.add((row,col))
                    q.append((row,col))

            return False

        l, r = 0, min(m[0][0], m[ROWS-1][COLS-1])
        res = l

        while l <= r:
            mid = (l+r)//2
            if feasible(mid):
                # if its feasible, that means we can try higher values so that a different path may be eligible
                res = mid
                l = mid+1
            else:
                # a feasible path from start to end wasnt found, so we have to try smaller values,
                r = mid -1


        return res

