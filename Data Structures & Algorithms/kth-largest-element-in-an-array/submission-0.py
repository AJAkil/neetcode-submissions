import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                # we fill in until we hit heap of size k
                heapq.heappush(heap, num)
            elif heap[0] <= num: # equal cause of sorted order
                # if the heap is full, we only let elements larger than
                # the root, cause the smaller one by definition can't be kthe largest, cause the root of the so-far developed heap is the k-th largest among the numbers we have processed
                heapq.heappushpop(heap, num)
            
        return heap[0]

        