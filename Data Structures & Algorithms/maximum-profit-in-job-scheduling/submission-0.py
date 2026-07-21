class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        index = list(range(n))
        index.sort(key=lambda i: startTime[i])
        memo = {}

        def dfs(i):
            # base case
            if i == n:
                return 0 # return 0 profit upon reaching end
            
            if i in memo:
                return memo[i]
            
            # we dont take the i-th job
            res = dfs(i+1)

            # if we take the ith job, we have to find out a job that doesnt overlap
            l, r , j = i + 1, n, n

            while l < r:
                mid = (l+r) // 2
                if startTime[index[mid]] >= endTime[index[i]]:
                    j = mid
                    r = mid
                else:
                    l = mid + 1

            res = max(res, profit[index[i]] + dfs(j))
            memo[i] = res

            return res
        
        return dfs(0)