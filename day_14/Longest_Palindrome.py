from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        occ = Counter(s)
        ln_longest = 0
        odd_exist = False
        for no_occ in occ.values():
            ln_longest += (no_occ // 2) * 2
            if no_occ % 2:
                odd_exist = True
        return ln_longest + 1 if odd_exist else ln_longest
