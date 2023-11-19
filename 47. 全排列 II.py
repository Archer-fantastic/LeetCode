from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2 and nums[0] == nums[1]:
            return [[nums[0], nums[1]]]
        ans = []
        for idx, num in enumerate(nums):

            nums[idx], nums[0] = nums[0], nums[idx]

            nums1 = self.permuteUnique(nums[1:])

            for idx, n in enumerate(nums1):
                nums1[idx].insert(0, nums[0])

            for _nums in nums1:
                if _nums not in ans:
                    ans.append(_nums)
        return ans