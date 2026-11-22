class UF:
	def __init__(self, n):
		self.par = [i for i in range(n)]
		self.size = [1] * n

	def find(self, u):
		if u == self.par[u]:
			return u

		self.par[u] = self.find(self.par[u])
		return self.par[u]

	def union(self, u,v):
		pu, pv = self.find(u), self.find(v)
		
		if pu == pv:
			return False

		if self.size[pu] >= self.size[pv]:
			self.par[pv] = pu
			self.size[pu] += self.size[pv]
		else:
			self.par[pu] = pv
			self.size[pv] += self.size[pu]

		return True
	
	def unmerge(self, u):
		self.par[u] = u # just reset it back to its own parent


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        time_map = {}
        # We construct the graph first
        for src, dst, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)

            time_map[time][src].append(dst)
            time_map[time][dst].append(src) # bidirectional graph

        uf = UF(n) # this takes O(n) time for the list.
        order = set()

        # we need to do union-find with the 0 and first person
        uf.union(0, firstPerson)
        order.add(0)
        order.add(firstPerson)

        for t in sorted(time_map.keys()):
            # we would go over them and union everything
            map_ = time_map[t]
            # we union each pair
            for src in map_.keys():
                for dst in map_[src]:
                    uf.union(src,dst)

            
            # now we check if any of the entire nodes in that set has a different parent than 0; if so, we need to unmerge them
            for src in map_.keys():
                if src not in order and uf.find(src) != uf.find(0): # messedup here, we need to compare parent of 0, not with 0, since a bigger cluster can merge later with the 0 cluster then the parent of 0 would change, this can happen say in later time steps, there are bigger clusters with some connection to the secret sharing cluster.
                    uf.unmerge(src)

                # else they know the secret
                else:
                    order.add(src)
            
        return list(order)
