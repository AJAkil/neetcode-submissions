import heapq
class Twitter:

    def __init__(self):
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweetmap[userId].append((tweetId, self.count))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # first we need to make the heap right with the tweets of the  members the userId is following + himself.
        # so we add himself to the members he follow
        self.followmap[userId].add(userId)

        # next we form the heap iterating the members he  follow
        for member_followed_id in self.followmap[userId]:
            if member_followed_id in self.tweetmap:
                # we start off from end of the tweets of the member the user follows
                index = len(self.tweetmap[member_followed_id]) - 1

                # we also need the timestamp of the tweet
                tweetId, count = self.tweetmap[member_followed_id][index]

                # then we start adding it to the max heap
                heapq.heappush(heap, [-1*count, member_followed_id, tweetId, index])
        

        # next we iterate the heap
        while heap and len(res) < 10:
            # we pop the object off the heap
            _, memberId, tweetId, index = heapq.heappop(heap)

            # we add to the result
            res.append(tweetId)

            # next we check if the previous id is valid
            if index - 1 >= 0:
                # then we again push that in the heap
                prev_tweetId, prev_count = self.tweetmap[memberId][index - 1]

                heapq.heappush(heap, [-1*prev_count, memberId, prev_tweetId, index - 1])

    
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
