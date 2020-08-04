# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def get_num(c_node):
        multiple = 1
        out = 0
        while c_node:
            out += c_node.val * multiple
            c_node = c_node.next
            multiple *= 10
        return out

    def create_revered_linkedList(num):
        head = ListNode()
        curr_node = head
        while num:
            curr_node.val = num % 10
            num = num // 10
            if num:
                curr_node.next = ListNode()
                curr_node = curr_node.next
        return head

    num_l1 = get_num(l1)
    num_l2 = get_num(l2)
    tot = num_l1 + num_l2
    return create_revered_linkedList(tot)


root_1 = ListNode(1)
root_1.next = ListNode(2)
root_1.next.next = ListNode(3)
root_2 = ListNode(1)
root_2.next = ListNode(2)
root_2.next.next = ListNode(3)
print(addTwoNumbers(root_1, root_2))
