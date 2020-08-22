import bisect
import random


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        area = 0
        self.ranges = [area]
        for x1, y1, x2, y2 in rects:
            area += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(area)

    def pick(self) -> List[int]:
        n = random.randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i - 1]
        n -= self.ranges[i - 1]
        width = x2 - x1 + 1
        return [x1 + n % width, y1 + n // width]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()