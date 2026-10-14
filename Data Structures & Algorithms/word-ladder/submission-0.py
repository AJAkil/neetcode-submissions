class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord == endWord or endWord not in wordList:
            return 0

        def get_nei(word):
            res = [] # returns the result here


            for i in range(len(word)):
                # we move from 'a' to 'z'
                for j in range(97, 123):
                    if word[i] == chr(j):
                        # we don't replace with the same words
                        continue

                    # else we make the new word by string slicing
                    nei_word = word[:i] + chr(j) + word[i+1:]

                    # next we check if the word is in the wordlist
                    # and append if it is
                    if nei_word in wordList:
                        res.append(nei_word)

            return res
        

        Q = deque([beginWord])
        visited = {beginWord}
        move = 0
        while len(Q)>0:
            for _ in range(len(Q)):
                curr_word_node = Q.popleft()
                if curr_word_node == endWord:
                    return move + 1

                for nei_node in get_nei(curr_word_node):
                    if nei_node not in visited:
                        visited.add(nei_node)
                        Q.append(nei_node)

        
            move += 1
        
        return 0



        