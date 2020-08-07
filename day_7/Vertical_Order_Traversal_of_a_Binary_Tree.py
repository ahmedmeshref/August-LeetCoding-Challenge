from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root):
    ele_q = deque()
    pos_q = deque()
    ele_q.append(root)
    pos_q.append(0)
    nodes_vals = []
    nodes_pos = []
    no_levels = 0
    while ele_q:
        no_levels += 1
        for _ in range(len(ele_q)):
            ele = ele_q.popleft()
            nodes_vals.append(ele.val)
            pos = pos_q.popleft()
            nodes_pos.append(pos)
            if ele.left:
                ele_q.append(ele.left)
                pos_q.append(pos - 1)
            if ele.right:
                ele_q.append(ele.right)
                pos_q.append(pos + 1)
    out = [[] for _ in range(abs(min(nodes_pos)) + max(nodes_pos) + 1)]
    for i in range(len(nodes_vals)):
        out[nodes_pos[i] + abs(min(nodes_pos))].append(nodes_vals[i])
    return out


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(verticalTraversal(root))
