import sys


def eraseOverlapIntervals(intervals: [[int]]) -> int:
    intervals.sort()
    rmved_interval = 0
    prev = -sys.maxsize
    for l, r in intervals:
        if l < prev:
            rmved_interval += 1
            if r > prev:
                continue
        prev = r
    return rmved_interval
