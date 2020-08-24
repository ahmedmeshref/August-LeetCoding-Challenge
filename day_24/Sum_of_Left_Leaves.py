from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        levels = deque()
        if root: levels.append(root)
        tot = 0
        while levels:
            for _ in range(len(levels)):
                curr_node = levels.popleft()
                if curr_node.left:
                    if not curr_node.left.left and not curr_node.left.right:
                        tot += curr_node.left.val
                    levels.append(curr_node.left)
                if curr_node.right:
                    levels.append(curr_node.right)
        return tot


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
tree = Solution()
print(tree.sumOfLeftLeaves(root))
