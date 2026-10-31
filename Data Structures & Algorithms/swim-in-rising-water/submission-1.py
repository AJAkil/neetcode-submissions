class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set() # for tracking which nodes I already visisted
        # the most important thing is the key
        # key = the smallest (maintained by the heap) maximum height required (condition of the problem) to reach neigboring cell. Because we want the minimum/smallest possible maximum height required to reach the final dest (n-1,n-1). So the key would give us minimum height that is maximum at any time.  
        minH = []
        heapq.heappush(minH, [grid[0][0], 0, 0]) # the first is the key

        visited.add((0,0)) # we add the starting cell
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N-1 and c == N-1:
                return t # that is the maximum time/height it will take to reach the end of the grid

            for dir_r, dir_c in dirs:
                n_r = r + dir_r
                n_c = c + dir_c

                if (n_r < 0 or n_r >= N or n_c < 0 or n_c >=N or (n_r, n_c) in visited):
                    continue
                
                # else we consider visiting what is popped off
                visited.add((n_r, n_c))

                heapq.heappush(minH, [
                    max(t, grid[n_r][n_c]),
                    n_r,
                    n_c
                ])