from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx+1]:
                nums[idx] *= 2
                nums[idx + 1] = 0
        count = 0
        ans = []
        for num in nums:
            if num == 0:
                count += 1
            else:
                ans.append(num)
        return ans + [0] * count
s = Solution()
print(s.applyOperations([1,2,2,1,1,0]))
print(s.applyOperations([0,1]))
print(s.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))