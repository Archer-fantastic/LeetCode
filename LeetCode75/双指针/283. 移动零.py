from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i,num in enumerate(nums):
            if num!=0:
                nums[idx]=num
                if i != idx:
                    nums[i] = 0
                idx += 1
