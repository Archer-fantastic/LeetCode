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
    # 160. 相交链表
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
    # 206. 反转链表
    def reverseList(self, head):
        cur_node = head
        new_head = ListNode()
        while cur_node:
            new_node = cur_node
            cur_node = cur_node.next
            new_node.next = new_head.next
            new_head.next = new_node
        return new_head.next

    # 234. 回文链表
    def isPalindrome(self, head):
        cur_node = head
        s = ""
        while cur_node:
            s += str(cur_node.val)
            cur_node = cur_node.next
        return s == s[::-1]
    # 141. 环形链表
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False
    # 142. 环形链表 II
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
    # 21. 合并两个有序链表
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
    # 24. 两两交换链表中的节点
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
    # 2. 两数相加
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = 0,0
        a,b = l1,l2
        tmp = 1
        while a:
            num1 = num1 + a.val * tmp
            tmp *= 10
            a = a.next
        tmp = 1
        while b:
            num2 = num2 + b.val * tmp
            tmp *= 10
            b = b.next
        num3 = num1 + num2
        # print(num1,num2,num3)
        head = ListNode()
        c = head
        if num3 == 0:
            return head
        while num3 > 0:
            c.next = ListNode(num3 % 10)
            c = c.next
            num3 //=10
        return head.next
    # 23. 合并 K 个升序链表
    def mergeKLists(self, lists):
        def mergeTwoList(a, b):
            head = ListNode()
            cur_node = head
            a_cur_node = a
            b_cur_node = b
            while a_cur_node and b_cur_node:
                if a_cur_node.val > b_cur_node.val:
                    cur_node.next = b_cur_node
                    b_cur_node = b_cur_node.next
                else:
                    cur_node.next = a_cur_node
                    a_cur_node = a_cur_node.next
                cur_node = cur_node.next
            if a_cur_node is not None:
                cur_node.next = a_cur_node
            if b_cur_node is not None:
                cur_node.next = b_cur_node
            return head.next

        if len(lists) > 0:
            head = lists[0]
        else:
            return None
        for l in lists[1:]:
            head = mergeTwoList(head, l)
        return head
    # 25. K 个一组翻转链表
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _len = get_len(head)
        count = _len // k
        new_head = ListNode()
        tail = new_head
        p = head
        for _ in range(count):
            for _ in range(k):
                q = p
                p = p.next
                q.next=tail.next
                tail.next = q
            for _ in range(k):
                tail = tail.next
        tail.next = p
        return new_head.next
# 146. LRU 缓存
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = {}
        self.stack = []


    def get(self, key):
        if key in self.pages:
            idx = self.stack.index(key)

            self.stack = self.stack[:idx] + self.stack[idx+1:]
            self.stack.append(key)

            return self.pages[key]
        else:
            return -1


    def put(self, key, value):
        if len(self.pages) == self.capacity and key not in self.pages:
            k = self.stack[0]
            self.stack.pop(0)
            self.stack.append(key)
            self.pages.pop(k)
            self.pages[key] = value
        else:
            if key in self.pages:
                idx = self.stack.index(key)
                self.stack = self.stack[:idx] + self.stack[idx + 1:]
                self.stack.append(key)
                self.pages[key] = value
            else:
                self.pages[key] = value
                self.stack.append(key)


s = Solution()
# printList(s.mergeTwoLists(array_init([1,2,4]), array_init([1,3,4])))
# printList(s.mergeTwoLists(None, array_init([1,3,4])))

# printList(s.addTwoNumbers(array_init([2,4,3]), array_init([5,6,4])))
# printList(s.addTwoNumbers(array_init([2,4,9]), array_init([5,6,4,9])))

printList(s.reverseKGroup(array_init([1,2,3,4,5]),2))

