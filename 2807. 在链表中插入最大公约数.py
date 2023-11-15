
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
