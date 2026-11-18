class Solution:
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Q = deque()
        h = []
        freq = Counter(tasks)
        t = 0

        # we form the heap first
        for item, f in freq.items():
            heapq.heappush(h, (-f, item)) 

        while Q or h:
            # first we check top of Q
            if Q and t >= Q[0][1]:
                # we push to the heap
                task, _ = Q.popleft()
                heapq.heappush(h, (-freq[task], task))
            
            # then we work with the heap
            if h:
                _, task = h[0]
                freq[task] -= 1
                heapq.heappop(h)
                if freq[task]>0:
                    Q.append((task, t + n + 1))
            t += 1

        return t
