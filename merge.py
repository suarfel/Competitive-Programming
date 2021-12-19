class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda element:element[0])
        i=0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] < intervals[i+1][1] :
                intervals[i][1] = intervals[i+1][1]
                intervals.remove(intervals[i+1])
                i = i
            elif intervals[i][1] >= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][1] :
                intervals.remove(intervals[i+1])
                i = i
            else:
                i = i + 1
        return intervals
        
        