from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = 2*max(nums)
        for i in range(len(nums)//2):
            ans = min(ans,(nums[i]+nums[len(nums)-1-i])/2)
        return abs