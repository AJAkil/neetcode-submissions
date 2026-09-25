import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # i get that we have to frequency map the array, 
        # say in example x x x y y x: 2 and y: 2 say and n = 2
        # now we choose x as its most frequent, lets say 
        # we use maxheap to choose x, we pop it off, then current max i # y but since we popped x off, we reduce its frequency in the map too, so does for y, but how do we track when to skip, everytime i pop off something, i know i have to skip S time when I have no more to run in the CPU for that element. say when popping of x, S = 2, when pop off y and we use y, S -= 1. now no more elemnt to run, we skip, S -= 1 = 0, now we can add again, but 

        # RES = x y - x y - x is an answer
        q = deque()
        heap = []
        time = 0

        freq_map = Counter(tasks)

        # we form the heap first
        for num, freq in freq_map.items():
            heapq.heappush(heap, (-freq, num)) # (freq first)

        
        while q or heap:
            # if either has anydata we continue

            if q and q[0][1] == time:
                    temp, _ = q.popleft()
                    # we push it back to the max heap acc to freq
                    heapq.heappush(heap, (-freq_map[temp], temp))
                
            if heap:
                # if heap has data, we have to schedule it now
                _, task_to_run = heap[0]
                # print(task_to_run)
                freq_map[task_to_run] -= 1 # we reduce the freq first
                heapq.heappop(heap) # we pop the element
               

                # now if freq > 0 we push it in Q again
                if freq_map[task_to_run] > 0:
                    q.append((task_to_run, time + n + 1))

            time += 1 # we proceed the time as we go
        
        return time




        


        