class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque, Counter

        # we form the map first
        freq = Counter(tasks)
        h = []
        time = 0
        Q = deque()

        # we form the heap
        for task, f in freq.items():
            heapq.heappush(h, (-f, task)) # O(TlogT) considering T unique items

        while h or Q:
            # first we check if there is something eligible in the Q
            if Q and time == Q[0][1]:
                # we push that to the heap
                task, _ = Q.popleft() # pop off Q # O(1)
                heapq.heappush(h, (-freq[task], task)) # O(logT)

            # then we work with the heap, 
            if h:
                # if the heap is not empty, something is ready to be scheduled
                _, next_task = heapq.heappop(h) # O(logT)
                
                freq[next_task] -= 1
                
                if freq[next_task] > 0:
                    # we can buffer it	
                    Q.append((next_task, time + 1 + n)) # next possible interva where we can schdule this # O(1)

            time += 1

        return time
