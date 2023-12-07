from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        stack = []
        n = len(nums)

        if sum(nums) < target:
            return 0

        cur_min = 0xFFFFFFFF
        cur_len = 0
        cur_sum = 0
        for num in nums:
            cur_len += 1
            cur_sum += num
            stack.append(num)
            while cur_sum >= target:
                cur_min = min(cur_min,cur_len)
                cur_sum -= stack.pop(0)
                cur_len -= 1
        return 0 if cur_min > n else cur_min
s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(s.minSubArrayLen(target = 4, nums = [1,4,4]))
print(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
print(s.minSubArrayLen(target = 11, nums = [2,2,2,2,2,2,2,2]))
print(s.minSubArrayLen(target = 11, nums = [1,2,3,4,5]))


