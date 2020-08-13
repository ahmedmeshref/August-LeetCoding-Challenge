from itertools import combinations


class CombinationIterator:
    """
    CombinationIterator takes a string characters of sorted distinct lowercase English letters and
        a number combinationLength as arguments.
    """
    def __init__(self, characters: str, combinationLength: int):
        self.comb = list(combinations(characters, combinationLength))
        self.ind = 0

    def next(self) -> str:
        """
        return the next combination of length combinationLength in lexicographical order.
        """
        if self.hasNext():
            val = ''.join(self.comb[self.ind])
            self.ind += 1
            return val

    def hasNext(self) -> bool:
        """
        return True if and only if there exists a next combination.
        """
        return len(self.comb) > self.ind

