class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        n, i, j, count = len(intervals), 0,1,0
        while i < n and j < n:
            cs, ce = intervals[i][0], intervals[i][1]
            ns, ne = intervals[j][0], intervals[j][1]
            if ce <= ns:
                i = j
                j+= 1
            else:
                count += 1
                if ce <= ne:
                    j += 1
                else:
                    i = j
                    j+= 1
        return count
        