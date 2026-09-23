import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = []
        self.K = k

        for item in nums:
            if len(self.kth_largest) < k:
                heapq.heappush(self.kth_largest, item)
            elif item > self.kth_largest[0]:
                heapq.heappushpop(self.kth_largest, item)
        

    def add(self, val: int) -> int:
        '''
                a max heap dont work cause we are not finding the largest rather kth largest
                and in a min heap of size k, we know the root is always the kth largst cause the largest one is in terminal leaf
        '''
        if len(self.kth_largest) < self.K:
            heapq.heappush(self.kth_largest, val)
        elif val > self.kth_largest[0]:
            heapq.heappushpop(self.kth_largest, val)
        
        return self.kth_largest[0]


        
