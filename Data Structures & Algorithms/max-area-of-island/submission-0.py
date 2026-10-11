class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c):
            # constraints here
            if (r < 0 or r == ROWS or c < 0 or c == COLS 
            or grid[r][c] == 0):
                # we dont do anything we skip and the area is basically 0
                return 0
            
            # else we can safely traverse.
            # as we are considering (r,c) as traversed and add 1+ for it,
            # we can safely mark it as 0
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r, c+1) + dfs(r+1,c) + dfs(r, c-1)



        area = 0 # if all are 0 area is 0 anyway
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))

        return area
                


        
        