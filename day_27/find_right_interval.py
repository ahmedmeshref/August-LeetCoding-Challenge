class Solution:
    def findRightInterval(self, intervals: [[int]]) -> [int]:
        """
        Given a set of intervals, for each of the interval i, check if there exists an interval j whose
         start point is bigger than or equal to the end point of the interval i, which can be called
         that j is on the "right" of i.
        """
        out = [-1 for _ in range(len(intervals))]
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort()
        for interval in intervals:
            l = 0
            r = len(intervals) - 1
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid][0] >= interval[1]:
                    out[interval[2]] = intervals[mid][2]
                    r = mid - 1
                else:
                    l = mid + 1
        return out
