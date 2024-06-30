class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(intervals)
        intervals = sorted(intervals)
        result.append(intervals[0])
        for i in range(1,n):
            if intervals[i][0]>result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1],result[-1][1])
        return result