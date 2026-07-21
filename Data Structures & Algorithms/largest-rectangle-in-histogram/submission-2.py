class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        
        for i in range(n):
            height = heights[i]

            r = i + 1
            l = i

            # we run two loops from i to get the r and l

            while r < n and heights[r] >= height:
                r += 1
            
            while l >= 0 and heights[l] >= height:
                l -= 1
            
            # then we adjust
            r -= 1
            l += 1

            max_area = max(height * (r-l+1), max_area)
        
        return max_area
        