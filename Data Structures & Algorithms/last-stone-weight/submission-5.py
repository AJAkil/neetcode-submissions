import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for item in stones:
            heapq.heappush(heap, -1*item)

        if len(heap) == 1:
            return -1*heap[0]
        
        while len(heap) > 1:
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)

            print(x,y)

            if x != y:
                to_insert = abs(x-y)
            
                heapq.heappush(heap, -1*to_insert)
            print(heap)
        
        print(heap)
        return -1*heap[0] if len(heap) >0 else 0
        

        