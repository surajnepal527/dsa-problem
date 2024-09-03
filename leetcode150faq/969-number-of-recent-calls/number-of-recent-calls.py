from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()
        
    #The problem is about returning the number of request with in range of t and 30000 
    #incusive
    #total number of request at each time
    # so everytime we get a request we insert it a top of th queue
    #we check the bottom value which is least possible value if that is not with in range 
    #we remove it so the next pointer is move one point left
    #we continue to check and pop left element till we find the element that is with in the range
    #we stop the loop and return the len of queue at that point.
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)