from typing import Optional


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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1、构造一个单调栈
        stack = []
        cur_node = head
        while cur_node:
            while len(stack) > 0 and cur_node.val > stack[-1].val:
                stack.pop()
            stack.append(cur_node)
            cur_node = cur_node.next

        # 2、根据单调栈构造出一个链表
        new_head = ListNode("head")
        cur_node = new_head
        for s in stack:
            cur_node.next = s
            cur_node = s
        cur_node.next = None
        return new_head.next

    def printList(self,l):
        current_node = l
        while current_node!=None:
            print(current_node,end='\t')
            current_node = current_node.next
        print()


l1 = array_init([18,6,10,3])
l2 = array_init([7])
l3 = array_init([5,2,13,3,8])
l4 = array_init([1,1,1,1])
s = Solution()
s.printList(s.removeNodes(l1))
s.printList(s.removeNodes(l2))
s.printList(s.removeNodes(l3))
s.printList(s.removeNodes(l4))
