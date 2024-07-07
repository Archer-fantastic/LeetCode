# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        cur_node = head
        while cur_node:
            if cur_node.val not in dic:
                dic[cur_node.val] = 1
            else:
                dic[cur_node.val] += 1

            cur_node = cur_node.next
        new_head = ListNode("input.txt head", next=head)
        pre = new_head
        cur_node = head
        while cur_node:
            if cur_node.val in dic and dic[cur_node.val] > 1:
                cur_node = cur_node.next
                pre.next = cur_node
            else:
                pre = cur_node
                cur_node = cur_node.next
        return new_head.next

