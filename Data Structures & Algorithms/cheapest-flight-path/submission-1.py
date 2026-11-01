class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))
        
        minH = []
        # the node state is (cost, node, stops_used_so_far)
        heapq.heappush(minH, [0, src, 0])
        visit = set()

        while minH:
            cost, city, stops_used = heapq.heappop(minH)

            if city == dst:
                return cost

            # if we already visited a node that has same city and stops used, we dont need to visit that again. Because the heap will always make sure that we visited a composite node in cheapest order so if we encounter a node/stte that is visited it is surely >= the previous cost.
            if (city, stops_used) in visit:
                continue
            
            visit.add((city, stops_used))
            
            # we skip if we hit a node that has already used k stops and so we do not need to expand that further
            if stops_used > k:
                continue
            
            for nei, nei_cost in adj[city]:
                heapq.heappush(minH,[
                    cost + nei_cost,
                    nei,
                    stops_used + 1
                ])
            
        return -1


        