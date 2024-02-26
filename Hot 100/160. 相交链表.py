from typing import Optional
def array_init(arr):
    head = ListNode(arr[0])
    cur_node = head
    for a in arr[1:]:
        new_node = ListNode(a)
        cur_node.next = new_node
        cur_node = cur_node.next
    return head


def get_len(l):
    current_node = l
    _len = 0
    while current_node is not None:
        _len += 1
        current_node = current_node.next
    return _len
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)


def printList(l):
    current_node = l
    while current_node!=None:
        print(current_node,end='\t')
        current_node = current_node.next
print()
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = get_len(headA)
        b = get_len(headB)
        while a != b:
            if a < b:
                headB = headB.next
                b -= 1
            elif a > b:
                headA = headA.next
                a -= 1
        while a > 0 or b > 0:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            a -= 1
            b -= 1
        return None

    def reverseList(self, head):
        cur_node = head
        new_head = ListNode()
        while cur_node:
            new_node = cur_node
            cur_node = cur_node.next
            new_node.next = new_head.next
            new_head.next = new_node
        return new_head.next

    def isPalindrome(self, head):
        cur_node = head
        s = ""
        while cur_node:
            s += str(cur_node.val)
            cur_node = cur_node.next
        return s == s[::-1]

    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        new_head = ListNode("T")
        c = new_head
        while a and b:
            if a.val < b.val:
                tmp = a
                a = a.next
            else:
                tmp = b
                b = b.next
            tmp.next = None
            c.next = tmp
            c = c.next
        if a:
            c.next = a
        if b:
            c.next = b
        return new_head.next

    # 19.删除链表的倒数第N个结点
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode("L")
        new_head.next = head
        _len = 0
        p = head
        while p:
            p = p.next
            _len += 1
        p = new_head
        for _ in range(_len - n):
            p = p.next
        p.next = p.next.next
        return head
        # 19.删除链表的倒数第N个结点
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode("L")
        new_head.next = head
        fast = new_head
        low = new_head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            low = low.next
        low.next = low.next.next
        return new_head.next
    # 148. 排序链表
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur =head
        n = 0
        res = []
        while cur:
            n+=1
            res.append(cur.val)
            cur = cur.next
        res.sort()
        cur =head
        n = len(res)
        m= 0
        while n>0:
            cur.val = res[m]
            m+=1
            cur = cur.next
            n-=1
        return head

s = Solution()
printList(s.mergeTwoLists(array_init([1,2,4]), array_init([1,3,4])))
printList(s.mergeTwoLists(None, array_init([1,3,4])))

