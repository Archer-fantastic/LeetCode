import collections
from typing import List


class Solution:
    # 136. 只出现一次的数字
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
    # 287. 寻找重复数

    def findDuplicate(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        for key in dic:
            if dic[key] > 1:
                return key
    # 75. 颜色分类
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = 0
        k = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                i += 1
            elif nums[idx] == 1:
                k += 1
            else:
                j += 1
        for idx in range(len(nums)):
            if idx < i:
                nums[idx] = 0
            elif idx < i+j:
                nums[idx] = 1
            else:
                nums[idx] = 2

        print(nums)

    def sortColors2(self, nums: List[int]) -> None:
        i = 0
        j = len(nums) - 1
        idx = 0
        while idx < j:
            if nums[idx] == 0:
                nums[i] = 0
                if idx != i:
                    nums[idx] = 1
                i += 1
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums[idx] = nums[j]
                nums[j] = 2
                j -= 1
        print(nums)