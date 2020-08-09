from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:
        rotten_q = deque()
        self.tot_fresh = 0

        def rotten(i, j):
            grid[i][j] = 2
            self.tot_fresh -= 1
            self.rotten = True
            return [i, j]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_q.append([i, j])
                elif grid[i][j] == 1:
                    self.tot_fresh += 1

        min_mins = 0
        while rotten_q:
            ln = len(rotten_q)
            self.rotten = False
            for _ in range(ln):
                i, j = rotten_q.popleft()
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    rotten_q.append(rotten(i - 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    rotten_q.append(rotten(i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    rotten_q.append(rotten(i, j - 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    rotten_q.append(rotten(i, j + 1))
            if self.rotten:
                min_mins += 1
        return min_mins if not self.tot_fresh else -1