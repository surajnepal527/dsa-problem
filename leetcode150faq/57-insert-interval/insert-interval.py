class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        inserted = False
        i = 0
        while i < len(intervals):
            #cas1 one
            if intervals[i][1] < newInterval[0]:
                i +=1
            elif intervals[i][0] > newInterval[1]:
                intervals.insert(i,newInterval)
                return intervals
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                del intervals[i]
        
        intervals.append(newInterval)
        return intervals


        