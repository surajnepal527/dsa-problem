import collections
class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count,tweetId))
        self.count -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap, res = [], []
        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
            tweets = self.tweetMap[follower]
            if tweets:
                tweet_idx = len(tweets)-1
                count, tweetId = tweets[tweet_idx]
                min_heap.append([count,tweet_idx,follower,tweetId])
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count,idx, follower, tweetId = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx > 0:
                count, tId = self.tweetMap[follower][idx-1]
                heapq.heappush(min_heap,[count, idx-1, follower,tId])
        
        return res




        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)