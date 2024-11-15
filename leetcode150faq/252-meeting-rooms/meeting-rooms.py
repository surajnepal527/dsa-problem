class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda i:i[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        for cur_start, cur_end in intervals[1:]:
            if cur_start < prev_end: return False
            prev_start = cur_start
            prev_end = cur_end
        return True
        