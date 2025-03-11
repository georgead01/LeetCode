# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    
    left = ListNode()
    right = ListNode()

    l = left
    r = right

    while head:
        if head.val < x:
            l.next = ListNode()
            l = l.next
            l.val = head.val
        else:
            r.next = ListNode()
            r = r.next
            r.val = head.val
        head = head.next

    print(left)
    print(right)

    if left.next:
        left = left.next
        right = right.next

        l.next = right
        return left
    else:
        return right.next