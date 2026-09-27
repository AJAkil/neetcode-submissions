import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        # [4 3 10 1 1 2]
        

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= -1*self.max_heap[0]:
            # push in the max heap
            heapq.heappush(self.max_heap, -1*num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # rebalance it here
        if len(self.max_heap) - len(self.min_heap) > 1:
            top_max_heap = -1*heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top_max_heap)
        
        if len(self.min_heap) - len(self.max_heap) > 1:
            top_min_heap = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*top_min_heap) # max heap

    def findMedian(self) -> float:
        res = 0
        if len(self.min_heap) == len(self.max_heap):
            # take the average
            res = (self.min_heap[0] + -1*self.max_heap[0])/2
        else:
            # take the top of element with the largest elements
            if len(self.min_heap) > len(self.max_heap):
                res = self.min_heap[0]
            else:
                res = -1*self.max_heap[0]
        
        return res
        
        