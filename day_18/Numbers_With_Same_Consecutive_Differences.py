class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def helper(num, ln):
            last_dig = num % 10
            if ln < N:
                num *= 10
                ln += 1
                if last_dig + K < 10:
                    helper(num + last_dig + K, ln)
                if last_dig - K >= 0:
                    helper(num + last_dig - K, ln)
            else:
                if not self.ans or num != self.ans[-1]:
                    self.ans.append(num)
                return
        self.ans = [] if N > 1 else [0]
        for i in range(1, 10):
            helper(i, 1)
        return self.ans 