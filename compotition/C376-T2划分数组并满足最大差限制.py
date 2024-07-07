from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(0,n,3):
            if nums[i+2] - nums[i] <= k:
                ans.append(nums[i:i+3])
            else:
                return []
        return ans
