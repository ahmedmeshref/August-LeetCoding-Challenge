"""Find the number of paths of a binary tree that sum to a given value."""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        q = deque()
        q.append([root, [root.val]])
        self.no_paths = 0
        while q:
            for _ in range(len(q)):
                node, r_sum = q.popleft()
                if node.val == target:
                    self.no_paths += 1
                if node.left:
                    q.append([node.left, self.helper(r_sum, node.left.val, target)])
                if node.right:
                    q.append([node.right, self.helper(r_sum, node.right.val, target)])
        return self.no_paths

    def helper(self, r_sum, node_val, target):
        sums = [node_val]
        for val in r_sum:
            c_sum = val + node_val
            if c_sum == target:
                self.no_paths += 1
            sums.append(c_sum)
        return sums


