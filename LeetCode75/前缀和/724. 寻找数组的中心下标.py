from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        for i in range(1,len(pre)):
            if pre[-1] - pre[i] == pre[i-1]:
                return i-1
        return -1