class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        time = 0
        fruit = 0
        Q = deque()
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruit += 1
                if grid[r][c] == 2:
                    Q.append((r,c))

        while Q and fruit > 0:
            # made mistake here, i thought of traversing each element of the Q one at a time, but no
            # this is the mistake to watch out for, since logically all rotten cell neighbors can be infected at the same time, we have to consider all the cells at a time. Besides, when infection is spreading, it will spread to the next of neighbors all at once each time step like spreading - so the pattern is when something is spreading temporally or one step a time, we consider all the current element in the Q together 
            length = len(Q)

            for i in range(length):
                # we consider all elements of the Q at the same time
                    row, col = Q.popleft()
                    for dr, dc in dirs:
                        n_r = row + dr
                        n_c = col + dc
                        
                        # then the out of bounds check
                        if n_r < 0 or n_r >= ROWS or n_c < 0 or n_c >= COLS or grid[n_r][n_c] == 0 or grid[n_r][n_c] == 2:
                            continue # we skip if empty or already rotten
                        
                        # else we spread the rotten/ infection to the healthy fruits/cell
                        Q.append((n_r, n_c))
                        grid[n_r][n_c] = 2
                        fruit -= 1 # we reduce the total number of fresh fruits/cell
                
                # this is a common pattern of level by dfs, when the entire level of the bfs tree is done, we increase the level counter/time by 1
            time += 1

        # after the bfs is done we check and return
        if fruit == 0: 
            return time

        return -1
