class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        
    # if either or both lists are empty, then merge is done
    if not list1:
        return list2
    if not list2:
        return list1

    # make sure list1 has smaller first val (or equal)
    if list1.val > list2.val:
        list1, list2 = list2, list1

    # set pointers
    ptr1 = list1
    ptr2 = list2

    # while there is still a next item
    while ptr1.next and ptr2.next:
        
        if ptr2.val <= ptr1.next.val:
            ptr1.next, ptr2.next, ptr2 = ptr2, ptr1.next, ptr2.next

        ptr1 = ptr1.next

    # sort the last element of list2 (if it exists), and get to the last element in list1
    while ptr1.next:
        if ptr2 and ptr2.val < ptr1.next.val:
            ptr1.next, ptr2.next, ptr2 = ptr2, ptr1.next, ptr2.next
            
        ptr1 = ptr1.next

    # if ptr2 still has elements, append them to end of list1
    if ptr2:
        ptr1.next = ptr2

    return list1

    # This algorithm is O(N).