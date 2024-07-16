# Definition for singly-linked list.
from typing import List, Optional



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
class Solution:
    def printList(self,l):
        current_node = l
        while current_node!=None:
            print(current_node,end='\t')
            current_node = current_node.next
        print()

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        m = max(nums)
        target = [0 for num in range(m+1)]
        for num in nums:
            target[num] = 1
        cur_node = head
        pre = head
        while cur_node:
            if cur_node.val<=m and target[cur_node.val] == 1:
                if cur_node == head:
                    head = head.next
                    pre = head
                    cur_node = head
                    continue
                else:
                    pre.next = cur_node.next
                    cur_node = cur_node.next
            else:
                if cur_node != head:
                    pre = cur_node
                cur_node = cur_node.next
        return head

s = Solution()
s.printList(s.modifiedList(nums = [1], head = array_init([1,2,1,2,1,2])))
s.printList(s.modifiedList(nums = [1,7,6,2,4], head = array_init([3,7,1,8,1])))