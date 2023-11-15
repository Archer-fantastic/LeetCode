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
    def __str__(self):
        return str(self.val)


class Solution(object):
    # def printList(self,l):
    #     current_node = l
    #     while current_node!=None:
    #         print(current_node,end='\t')
    #         current_node = current_node.next
    #     print()
    def addTwoNumbers(self, l1, l2):
        len_1 = get_len(l1)
        len_2 = get_len(l2)
        p_l1 = l1
        p_l2 = l2
        while None != p_l1.next:
            p_l1 = p_l1.next
        while None != p_l2.next:
            p_l2 = p_l2.next
        while len_1 < len_2:
            zero_node = ListNode()
            p_l1.next = zero_node
            p_l1 = zero_node
            len_1 += 1
        while len_1 > len_2:
            zero_node = ListNode()
            p_l2.next = zero_node
            p_l2 = zero_node
            len_2 += 1
        # s.printList(l1)
        # s.printList(l2)

        target = 0
        p_l1 = l1
        p_l2 = l2
        p_l3 = ListNode()
        l3 = p_l3
        while p_l1 != None:
            val_1 = p_l1.val
            val_2 = p_l2.val
            p_l3.next = ListNode((val_1+val_2+target)%10)
            p_l3 = p_l3.next
            if val_1+val_2+target >= 10:
                target = 1
            else:
                target = 0
            p_l1 = p_l1.next
            p_l2 = p_l2.next
        if target > 0:
            p_l3.next = ListNode(1)
        # self.printList(l3.next)
        return l3.next