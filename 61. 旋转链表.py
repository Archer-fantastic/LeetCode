# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_len(self, head):
        _len = 0
        while head:
            head = head.next
            _len += 1
        return _len

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        _len = self.get_len(head)
        if _len <= 1:
            return head
        k = k % _len
        count = 0
        cur_node = head

        while cur_node:
            count += 1
            if count == _len - k:
                new_head = cur_node
            if count == _len:
                new_tail = cur_node
            cur_node = cur_node.next
        new_tail.next = head
        head = new_head.next
        new_head.next = None
        return head
