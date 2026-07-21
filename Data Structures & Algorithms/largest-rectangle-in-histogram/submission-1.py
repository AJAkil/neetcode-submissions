class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = [] #(index, height)
        
        
        for i, h in enumerate(heights):
            start = i

            # monotonically increasing stack, broken when we hit a 
            # rectangle with a lower height than ours, we need to pop if off
            while stack and h < stack[-1][1]: 
                index, height = stack.pop()
                # this would take care of the left extension when we compute the area
                max_area = max(max_area, height * (i - index))
                start = index
            
            stack.append((start, h))
        
        # we still might have some elements in the stack,
        # so for the elements, they can be extended to the end of the array,
        # so the width of the rectangles formed by them will be (n-index) 

        for i, h in stack:
            max_area = max(max_area, h * (n - i))
        
        return max_area
        