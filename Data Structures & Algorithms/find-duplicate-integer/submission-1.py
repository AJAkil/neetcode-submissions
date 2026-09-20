class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num 
        #     # if not we add it to the set
        #     seen.add(num)
        l = 1
        n = len(nums) - 1
        r = n

        while l < r:
            mid = (l+r)//2 # in answer space
            sum_up_mid = sum(1 for num in nums if num <=mid)

            if sum_up_mid <= mid:
                # duplicates must be in the right part
                l = mid + 1
            else:
                # which means duplicates are in the left part
                r = mid
            
        return l



    '''
    [1,2,3,3,3]
    [1,2,3,4] mid = 2, l = 1 and r = 4
    (1,2) -> count(nums) = 2 expected if no duplicate 1,2 so 4 so duplicates are in that range upto <= mid sp l = 1 , r = mid
    (l,r) (1,2) mid = 1
    count(nums) upto <= 1 = 1 so we good l = mid+1 = 2, r = mid 
    since l == r, return l = 2 which is the answer


    next look to mid+1 to r - [3,4] - mid = 3
    count (nums) upto 3 =  5 if no duplicate 1,2,3 since its 5 upto the mid, so there is a duplicate, so l = 3, r= mid = 3
    when l == r we at the sol return that?
    logn
    '''


        