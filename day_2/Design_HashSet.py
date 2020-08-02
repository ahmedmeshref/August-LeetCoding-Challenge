class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 12000
        self.hashSet = [[] for i in range(self.buckets)]

    def hash_function(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        hash_key = self.hash_function(key)
        if key not in self.hashSet[hash_key]:
            self.hashSet[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash_function(key)
        for i in range(len(self.hashSet[hash_key])):
            if self.hashSet[hash_key][i] != key:
                continue
            self.hashSet[hash_key].pop(i)
            break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = self.hash_function(key)
        return key in self.hashSet[hash_key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)