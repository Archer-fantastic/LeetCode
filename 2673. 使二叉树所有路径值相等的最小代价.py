import math
from typing import List
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"[{self.val},{self.left},{self.right}]"
def bulid_tree(l):
    l.insert(0,None)
    return init_tree(l,1)
def init_tree(l,idx):
    # l = [null,1,2,3,4,5,null,6,7,null,null,null,null,8]
    if idx >= len(l):
        return None
    if l[idx] is None:
        return None
    tree = TreeNode(l[idx])
    if idx * 2 >= len(l):
        tree.left = None
    if idx * 2 + 1 >= len(l):
        tree.right = None
    tree.left = init_tree(l,2*idx)
    tree.right = init_tree(l,2*idx+1)
    return tree


class Solution:
    def minIncrements1(self, n: int, cost: List[int]) -> int:
        _len = math.log2(n+1)
        visit = [0 for _ in range(len(cost))]
        s = [0]
        while len(s) > 0:
            idx = s[-1]
            if 2*idx + 1 < n and visit[2*idx + 1] == 0:
                s.append(2*idx + 1)
            elif 2*idx + 2 < n and visit[2*idx + 2] == 0:
                s.append(2*idx + 2)
            else:
                visit[s.pop()] = 1

            if len(s) == _len:
                _sum = 0
                for ss in s:
                    print(cost[ss],end=" ")
                    _sum += cost[ss]

                print(_sum)
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range((n-2)//2,-1,-1):
            ans += abs(cost[2*i+1]-cost[2*i+2])
            cost[i] += max(cost[i * 2 + 1], cost[i * 2+2])
        return ans
s = Solution()
print(s.minIncrements(n = 7, cost = [1,5,2,2,3,3,1]))
print(s.minIncrements(n = 3, cost = [5,3,3]))
print(s.minIncrements(n = 15, cost = [764,1460,2664,764,2725,4556,5305,8829,5064,5929,7660,6321,4830,7055,3761]))


