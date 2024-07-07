from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        res = []
        for idx in range(0, len(nums), 2):
            res.append(nums[idx + 1])
            res.append(nums[idx])
        return res