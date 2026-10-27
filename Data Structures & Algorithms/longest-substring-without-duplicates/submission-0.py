class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        c = 0
        pos = {}

        for r in range(len(s)):
            if s[r] in pos:
                # we update the left pointer
                l = max(l, pos[s[r]]+1) # max so we don't prevent it to go left that was in old window
            
            pos[s[r]] = r # we update the position of what we have seen so far      
            c = max(c, r - l + 1)
        
        return c
            



