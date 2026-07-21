class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l,r = 0, len(matrix[0])
        t,b = 0, len(matrix)

        while l<r and t<b:
            for i in range(l, r):
                res.append(matrix[t][i])
        
            # we move top for next right turn
            t += 1

            for i in range(t, b):
                res.append(matrix[i][r-1])

            '''
            1 2 3 4
            5 6 7 8
            9 10 11 12
            '''
            
            # we move right pointer back by 1
            r -= 1

            if not (l<r and t<b):
                break

            for i in range(r-1, l-1 ,-1):
                res.append(matrix[b-1][i])
            
            # move bottom pointer up by 1
            b -= 1

            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            
            # we start on inner spiral, so increase left by 1
            l += 1
        return res


        