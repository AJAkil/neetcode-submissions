class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            # update the map
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            # now as we move right, we check the window violation here
            # the valid condition of replacement
            '''
            character to replace <= k
            w_size - most_freq_seen_so_far <= k
            so invalid = w_size - most_freq_seen_so_far >k
            '''
            
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
        