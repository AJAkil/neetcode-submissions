class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        l,r = 0,0
        n = len(grid)

        for row in range(n):
            l = min(l, min(grid[row]))
            r = max(r, max(grid[row]))
        
        
        def dfs(r,c,t):
            if r < 0 or r >= n or c < 0 or c >=n or ((r,c) in visited) or grid[r][c] > t:
                return False
            
            # check if we have reached the end of the cell
            if r == n-1 and c == n-1:
                return True 

            # we have looked at that cell
            visited.add((r,c))

            # next we run the dfs
            return (
                dfs(r-1, c, t) or
                dfs(r + 1, c,t) or
                dfs( r, c+1, t) or
                dfs(r, c-1,t)
            )


        # the actual binary search

        while l < r:
            m = (l+r)//2

            visited = set()
            if dfs(0,0,m):
                r = m
            else:
                l = m + 1
        
        return l

            



            






