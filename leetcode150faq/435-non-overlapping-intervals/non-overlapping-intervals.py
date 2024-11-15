class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        output = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                output += 1
                if prev_end > end:                
                    prev_start = start
                    prev_end = end
            else:
                prev_start = start
                prev_end = end
                
        return output
        