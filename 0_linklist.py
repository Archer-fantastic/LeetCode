
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

    def reserve_list(self, head):
        cur_node = head
        new_head = ListNode()
        while cur_node:
            new_node = ListNode(cur_node.val)
            new_node.next = new_head.next
            new_head.next = new_node
            cur_node = cur_node.next
        return new_head.next
    def detectCycle(self, head):
        '''
        检测链表是否有环
        :param head:
        :return:
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None
    def get_len(self,head):
        '''
        获取链表长度
        :param head:
        :return:
        '''
        _len = 0
        while head:
            head = head.next
            _len += 1
        return _len
    def rotateRight(self, head, k):
        """
        旋转链表 右循环k位
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        _len = self.get_len(head)
        k = k%_len
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
    def removeNthFromEnd(self, head, n):
        """
        删除链表的倒数第n个节点
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
    def mergeTwoLists(self, list1, list2):
        '''
        合并两个升序链表
        :param list1:
        :param list2:
        :return:
        '''
        pl1 = list1
        pl2 = list2
        list3 = ListNode()
        pl3 = list3

        while pl1 or pl2:
            if pl1 is None:
                pl3.next = pl2
                break
            if pl2 is None:
                pl3.next = pl1
                break
            val1 = pl1.val
            val2 = pl2.val
            if val1 <= val2:
                pl3.next = ListNode(val1)
                pl1 = pl1.next
            else:
                pl3.next = ListNode(val2)
                pl2 = pl2.next
            pl3 = pl3.next
        return list3.next
    def mergeKLists(self, lists):
        """
        合并k个有序链表
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) > 0:
            head = lists[0]
        else:
            return lists
        for l in lists[1:]:
            head = self.mergeTwoList(head,l)
        return head
    def swapPairs(self, head):
        """
        两两交换链表节点
        :type head: ListNode
        :rtype: ListNode
        """
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
        # self.printList(head_node.next)
        return head_node.next



    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a,b):
            for num in range(int(min(a,b)),0,-1):
                if a % num == 0 and b % num == 0:
                    return num
            return 1

        cur_node = head
        while cur_node.next:
            new_node = ListNode(gcd(cur_node.val,cur_node.next.val),cur_node.next)
            cur_node.next = new_node
            cur_node = cur_node.next.next
        return head
l1 = array_init([18,6,10,3])
l2 = array_init([7])
s = Solution()
print(s.printList(s.insertGreatestCommonDivisors(l1)))
print(s.printList(s.insertGreatestCommonDivisors(l2)))
