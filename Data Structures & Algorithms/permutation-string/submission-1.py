class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = Counter(s1)
        m2 = Counter()
        l = 0
        l_s1 = len(s1)

        for r in range(len(s2)):
            c = s2[r]
            m2[c] += 1

            # then we check the invalid cond here again
            while m2[c] > m1[c]:
                # we found something extra here so its invalid,
                # we shrink the window
                m2[s2[l]] -= 1
                l += 1
            
            if r-l+1 == l_s1:
                return True
        

        return False
        