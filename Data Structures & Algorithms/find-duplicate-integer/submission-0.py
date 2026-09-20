class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num 
            # if not we add it to the set
            seen.add(num)
        