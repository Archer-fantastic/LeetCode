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

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
            num = num*10 + cur.val
            cur = cur.next

        num = num * 2

        new_head = ListNode("head")

        while num > 0:
            r = num % 10
            node = ListNode(r,new_head.next)
            new_head.next = node
            num //= 10

        return new_head.next
s = Solution()
s.printList(s.doubleIt(array_init([1,2,3])))
s.printList(s.doubleIt(array_init([0])))