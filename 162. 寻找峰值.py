import math


class Solution(object):
    def findPeakElement(self, nums):
        nums = [-math.inf] + nums + [-math.inf]
        for idx in range(1,len(nums)-1):
            if nums[idx-1] < nums[idx] and nums[idx+1] < nums[idx]:
                return idx - 1
s = Solution()
print(s.findPeakElement([1,2,3,1]))