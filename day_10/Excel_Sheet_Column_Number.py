import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        d = dict(zip(string.ascii_uppercase, range(1, 27)))
        ln = len(s)
        for ind in range(ln):
            ans += (26 ** ind) * (d[s[ln - 1 - ind]])
        return ans
