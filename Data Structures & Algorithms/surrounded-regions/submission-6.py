class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c]!='O'):
                return
            
            # else we mark it as x as its surrounded
            board[r][c] = '-'
            # we go ahead with dfs
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # we have to mark them as non eligible to be captured
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '-':
                    board[r][c] = 'O'
        