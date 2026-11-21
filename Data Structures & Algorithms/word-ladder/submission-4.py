from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # cat wordList = [mat, mag, sag] target = sag
        # cat -> [mat] t = 1
        # mat -> [mag] t = 2
        # mag -> sag t =. 3

        Q = deque()
        visited = set()

        Q.append(beginWord)
        visited.add(beginWord)
        wordList = set(wordList)
        turn = 0

        def get_nei(node):
            res = []
            for i in range(len(node)):
                for j in range(97, 123):
                    if node[i] == chr(j):
                        continue # skipping changing the same character

                    word = node[:i] + chr(j) + node[i+1:]
                    if word in wordList:
                        res.append(word)	
            
            return res


        while Q:
            n = len(Q)
            for _ in range(n):
                node = Q.popleft()
                if node == endWord:
                    return turn + 1

                for nei in get_nei(node):
                    if nei not in visited:
                        visited.add(nei)
                        Q.append(nei)
            
            turn += 1

        return 0

        