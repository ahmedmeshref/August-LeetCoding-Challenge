import re


def isPalindrome(s: str) -> bool:
    s = "".join(re.findall(r"[A-Za-z0-9]+", s))
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

