from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            nums[idx] = nums[idx]%2
        res1 = 1
        res2 = max(nums.count(0),nums.count(1))
        a = nums[0]
        for idx in range(1,len(nums)):
            if (a + nums[idx]) % 2 == 1:
                res1 += 1
                a = nums[idx]
        return max(res1,res2)
s = Solution()
print(s.maximumLength(nums = [1,2,3,4]))
print(s.maximumLength(nums = [1,2,1,1,2,1,2]))
print(s.maximumLength(nums = [1,3]))
print(s.maximumLength(nums = [1,5,9,4,2]))
print(s.maximumLength(nums = [1,7,8,7,5]))
