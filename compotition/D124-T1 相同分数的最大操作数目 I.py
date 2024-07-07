from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        num = nums[0] + nums[1]
        count = 0
        for idx in range(0,len(nums),2):
            if idx+1 <= len(nums)-1 and nums[idx]+nums[idx+1] == num:
                count +=1
            else:
                break
        return count

s = Solution()
print(s.maxOperations([1,1,1,1,1,1]))