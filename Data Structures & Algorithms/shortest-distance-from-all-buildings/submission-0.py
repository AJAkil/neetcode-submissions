class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(-1,0), (0,1),(1,0),(0,-1)]

        total_houses = 0

        # create a 2d array that tracks (distance to houses sum, 
        # how many houses visited it)
        distances = [[[0,0] for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(start_r, start_c):
            q = deque()
            visited = set((start_r, start_c))

            dist = 0 
            q.append((start_r, start_c))

            while q:
                for _ in range(len(q)): # since we need to compute distances
                    r, c = q.popleft()

                    if grid[r][c] == 0:
                        # only do this if its a land
                        distances[r][c][0] += dist
                        distances[r][c][1] += 1
                    
                    for dir_r, dir_c in dirs:
                        n_r, n_c = r + dir_r, c + dir_c

                        if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 0:
                            
                            if (n_r,n_c) in visited:
                                continue
                            
                            q.append((n_r, n_c))
                            visited.add((n_r, n_c))
                dist += 1


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    # itsa house, do bfs from here
                    bfs(i,j)
                    total_houses += 1

        
        # now get the eligable cells with the minimum dist
        min_dist = float('inf')

        for i in range(ROWS):
            for j in range(COLS):
                if distances[i][j][1] == total_houses:
                    min_dist = min(min_dist, distances[i][j][0])
        
        return -1 if min_dist == float('inf') else min_dist

        