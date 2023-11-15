def get_len(l):
    current_node = l
    _len = 0
    while current_node != None:
        _len += 1
        current_node = current_node.next
    return _len

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        _len = get_len(head)
        cur_node = head
        count = 1
        if _len == n:
            return head.next
        while cur_node:
            if count == _len - n:
                cur_node.next = cur_node.next.next
                return head
            count += 1
            cur_node = cur_node.next