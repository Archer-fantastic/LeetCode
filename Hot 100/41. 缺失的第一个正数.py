from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        num = 1
        idx = 0
        n =len(nums)
        while idx < n and nums[idx] <= num:
            if nums[idx] == num:
                num += 1
            idx += 1
        return num
s = Solution()
print(s.firstMissingPositive(nums = [1,2,0]))
print(s.firstMissingPositive(nums = [3,4,-1,1]))
print(s.firstMissingPositive(nums = [7,8,9,11,12]))