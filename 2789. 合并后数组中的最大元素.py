from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        nums = nums[::-1]
        ans = nums[0]
        cur_sum = nums[0]
        for idx in range(len(nums)-1):
            if cur_sum >= nums[idx+1]:
                cur_sum += nums[idx+1]
            else:
                cur_sum = nums[idx+1]
            ans = max(ans,cur_sum)
        return ans


s = Solution()
print(s.maxArrayValue([2,3,7,9,3]))
print(s.maxArrayValue([5,3,3]))
print(s.maxArrayValue([77]))