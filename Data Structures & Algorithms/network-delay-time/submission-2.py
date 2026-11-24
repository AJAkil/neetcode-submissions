class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        t  = -1
        visited =set()
        adj = {i: [] for i in range(1, n+1)}
        h = []
        # form the adjacency list first
        for u, v, w in times:
            adj[u].append((v,w))
            
        heapq.heappush(h, (0,k))

        while h:
            w_curr, u = heapq.heappop(h)

            if u in visited:
                continue

            t = w_curr
            visited.add(u)
            
            for v,w_nei in adj[u]:
                heapq.heappush(h, (w_curr + w_nei, v))

        print(visited)
        return t if len(visited) == n else -1
