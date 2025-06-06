class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]
        for right_start, right_end in intervals[1:]:
            left_end = res[-1][1]
            if right_start <= left_end:
                res[-1][1] = max(left_end, right_end)
            else:
                res.append([right_start, right_end])   
        return res
        