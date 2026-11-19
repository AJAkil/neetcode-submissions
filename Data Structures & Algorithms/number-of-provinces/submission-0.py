class UF:
	def __init__(self,n):
		self.parent = list(range(n))
		self.sizes = [1] * (n) # for safety
		
	
	def find(self,n):
		if self.parent[n] == n:
			return  n
		self.parent[n] = self.find(self.parent[n])

		return self.parent[n]
		

	def union(self,u,v):
		pu = self.find(u)
		pv = self.find(v)

		if pu == pv:
			return False
		
		if self.sizes[pu] >= self.sizes[pv]:
			# merge v to u
			self.parent[pv] = pu
			self.sizes[pu] += self.sizes[pv] # v is being absorbed to u
			
		else:
			self.parent[pu] = pv
			self.sizes[pv] += self.sizes[pu]
			
		
		return True



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # now we traverse the graph
        N = len(isConnected)
        uf = UF(N)
        total = N

        for i in range(N):
            for j in range(N):
                if  i!=j and isConnected[i][j] == 1:
                    if uf.union(i,j):
                        total -= 1


        return total
        