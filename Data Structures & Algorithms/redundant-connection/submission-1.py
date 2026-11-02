class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)] # each is its own parent
        rank = [1] * (N+1)

        def find(n):
            if n!=par[n]:
                par[n] = find(par[n])
            
            return par[n]
        

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                # both of their parents are same, so in the disjoint set, they are part of the same set/tree, hence, this last edge for which they are part of the same tree is the cycle creating set.
                return [n1,n2]
            

            

        