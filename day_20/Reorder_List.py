# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next

        curr = head
        while curr and curr.next:
            last_node = nodes.pop()
            if last_node is not curr.next:
                nodes[-1].next = None
                last_node.next = curr.next
                curr.next = last_node
                curr = last_node.next
            else:
                curr = curr.next
        return head