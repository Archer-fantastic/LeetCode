
class Solution(object):
    def swapPairs(self, head):
        head_node = ListNode()
        head_node.next = head
        front_node = head_node
        cur_node = head
        while cur_node and cur_node.next:
            front_node.next = cur_node.next
            cur_node.next = cur_node.next.next
            front_node.next.next = cur_node
            front_node = cur_node
            cur_node = front_node.next
        return head_node.next