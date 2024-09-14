class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)
        i = 0
        j = 1
        count = 0
        while j < n:
            cs = intervals[i][0]
            ce = intervals[i][1]
            ns = intervals[j][0]
            ne = intervals[j][1]

            if ce > ns:
                if ce <= ne:
                    j += 1
                else:
                    i = j
                    j += 1
                count += 1
            else:
                i = j
                j += 1

        return count    
                
