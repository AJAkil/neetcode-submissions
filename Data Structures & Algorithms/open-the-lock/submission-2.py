from collections import deque
def get_nei(node):
            res = []
            # since we have four slots, we do this
            for i in range(4):
                digit = int(node[i])
                next_ = (digit + 1) % 10
                prev_ = (digit - 1) % 10

                res.append(node[:i] + str(next_) + node[i+1:])
                res.append(node[:i] + str(prev_) + node[i+1:])

            return res

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
            
        Q = deque()
        visited = set(deadends) # we can start off with these deadends since they won't be considered for expansion anyway
        turns  = 0

        if '0000' in visited:
            return -1

        Q.append('0000') # we start with the initial state
        visited.add('0000') # we need to add this too sorry

        

        while Q:
            n = len(Q) # level wise bfs for shortest path
            
            for _ in range(n):
                node = Q.popleft() # we get the current state or the node here
                if node == target:
                    return turns
                for nei in get_nei(node):
                    if nei not in visited:
                        # we add them to visited and the Q
                        Q.append(nei)
                        visited.add(nei)
            
            # when the level finishes, we increase the counter by1
            turns += 1


        return -1
