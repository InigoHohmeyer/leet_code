
#Class Definition for our Nodes:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Our Linked Lists
l1_3 = ListNode(4)
l1_2 = ListNode(2, l1_3)
l1 = ListNode(1, l1_2)
l2_3 = ListNode(4)
l2_2 = ListNode(3, l2_3)
l2 = ListNode(1, l2_2)


def mergeTwoSortedLists(list1, list2):
    #   This will be the head of the list that we will return
    return_head = ListNode
    tail = ListNode
    return_head.next = tail
    #   We set the lower value list to the return head, and then we
    #   iterate that head forward to the next node
    if list1.val < list2.val:
        return_head = list1
        list1 = list1.next
    else:
        return_head = list2
        list2 = list2.next
    print(f'this is the return_head value {return_head.val}')
    #  The loop continues while both list1 and list2 are not None
    while list1 is not None and list2 is not None:
        #   Executes if list1 has reached the end or list2 is smaller
        if list1 is None:
            #  Appends list2 to the end of the tail
            tail.next = list2
        elif list2 is None:
            tail.next = list1
        elif list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        elif list2.val < list1.val:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    return return_head
# list1 = 1,2,4
# list2 = 1,3,4
#Method for printing Linked List
def PrintLinked(node):
    while node:
        print(node.val)
        node = node.next
PrintLinked(mergeTwoSortedLists(l1, l2))

