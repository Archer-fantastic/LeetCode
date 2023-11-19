# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reserve_list(self, head):
        cur_node = head
        new_head = ListNode()
        while cur_node:
            new_node = ListNode(cur_node.val)
            new_node.next = new_head.next
            new_head.next = new_node
            cur_node = cur_node.next
        return new_head.next

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        head_node = ListNode("head", head)
        cur_node = head_node
        count = 0
        while cur_node:
            if count == left - 1:
                left_node = cur_node
            if count == right:
                right_node = cur_node.next
                cur_node.next = None
                break
            cur_node = cur_node.next
            count += 1
        mid = self.reserve_list(left_node.next)

        left_node.next = mid
        cur_node = mid
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = right_node
        return head_node.next
