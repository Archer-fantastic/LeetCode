import random
from typing import Optional


def get_len(l):
    current_node = l
    _len = 0
    while current_node != None:
        _len += 1
        current_node = current_node.next
    return _len
def array_init(arr):
    head = ListNode(arr[0])
    cur_node = head
    for a in arr[1:]:
        new_node = ListNode(a)
        cur_node.next = new_node
        cur_node = cur_node.next
    return head
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)


class Solution(object):
    def printList(self,l):
        current_node = l
        while current_node!=None:
            print(current_node,end='\t')
            current_node = current_node.next
        print()

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        my_head = ListNode("head")
        my_head.next = head
        left_node = my_head
        while left_node.next and left_node.next.val < x:
            left_node = left_node.next
        cur_node = left_node.next
        pre_node = left_node
        while cur_node:
            if cur_node.val < x:
                pre_node.next = cur_node.next
                cur_node.next = left_node.next
                left_node.next = cur_node
                left_node = cur_node
                cur_node =pre_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return my_head.next
s = Solution()
head1 = array_init([1,4,3,2,5,2])
s.printList(head1)
s.printList(s.partition(head1,3))

head3 = array_init([2,1])
s.printList(head1)
s.printList(s.partition(head3,2))

head4 = array_init([10,9,8,7,7,5,4,3,2,1,11])
s.printList(head4)
s.printList(s.partition(head4,6))

# head2 = array_init([random.randint(1,100) for _ in range(100)])
# s.printList(head2)
# s.printList(s.partition(head2,50))


