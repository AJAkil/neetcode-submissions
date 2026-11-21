class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
        ]

        def dfs(r,c):
            # base case first
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            # else we consider it to be visitable
            grid[r][c] = "0"
            
            for dr, dc in dirs:
                dfs(r+dr, c+dc)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1

        return res
