class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        

        mH = [(0,k)]
        visited = set()
        t = 0

        while mH:
            w_c, n_c = heapq.heappop(mH)

            if n_c in visited:
                continue
            
            visited.add(n_c)
            t = w_c
            
            for n_nei, w_nei in edges[n_c]:
                heapq.heappush(mH, (w_nei + w_c, n_nei))
        
        return t if len(visited)==n else -1



        