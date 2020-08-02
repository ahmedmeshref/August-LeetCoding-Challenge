"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1- All letters in this word are capitals, like "USA".
2- All letters in this word are not capitals, like "leetcode".
3- Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""

import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word or re.search(r"(^[A-Z]{1}[a-z]*$|^[a-z]+$|^[A-Z]+$)", word):
            return True
        else:
            return False

