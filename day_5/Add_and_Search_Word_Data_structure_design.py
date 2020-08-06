class Trie:
    def __init__(self, val=None):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr.setdefault("end", True)

    def search(self, word: str, curr=None) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not self.root:
            return False
        if not curr:
            curr = self.root
        for ind in range(len(word)):
            if word[ind] == ".":
                for key in curr.keys():
                    if "end" != key and self.search(word[ind + 1:], curr[key]):
                        return True
            else:
                if word[ind] not in curr:
                    return False
            try:
                curr = curr[word[ind]]
            except KeyError:
                return False
        return True if "end" in curr else False


new_trie = Trie()
# new_trie.insert("ahmed")
new_trie.insert("a")
new_trie.insert("bad")
print(new_trie.search("bad"))
