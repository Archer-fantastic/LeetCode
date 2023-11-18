import bisect
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums,reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        # print(self.nums)
        self.bin_insert(val)
        return self.nums[self.k-1]
    def bin_insert(self,val):
        left = 0
        right = len(self.nums) - 1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] == val:
                idx = mid
                break
            elif self.nums[mid] > val:
                left = mid + 1
            else:
                right = mid - 1
        if idx == -1:
            idx = left
        self.nums.insert(idx,val)
def fun(commands,parms):
    obj = KthLargest(parms[0][0],parms[0][1])
    n = len(commands)
    for i in range(1,n):
        print(f"round {i}",end=" ")
        if commands[i] == "add":
            print(obj.add(parms[i][0]))

fun(["KthLargest", "add", "add", "add", "add", "add"],[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]])


