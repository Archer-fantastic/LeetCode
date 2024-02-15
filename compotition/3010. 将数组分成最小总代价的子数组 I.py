from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        l =sorted(nums[1:])
        return nums[0] + l[0] + l[1]

s = Solution()
print(s.minimumCost([1,2,3,12]))
print(s.minimumCost([10,2,3,1]))
print(s.minimumCost([10,3,1,1]))