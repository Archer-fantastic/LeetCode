from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def fun(nums):
            cnt = 0
            _max = 0
            for num in nums:
                if num == 1:
                    cnt += 1
                    _max = max(_max,cnt)
                else:
                    cnt = 0
            return _max
        if k == 0: return fun(nums)
        left = 0
        _max = 0
        right = 0
        one_cnt = 0
        zero_cnt = 0
        n = len(nums)

        while right < n:
            if nums[right] == 1:
                right += 1
                one_cnt += 1
                _max = max(_max,one_cnt)
            else:
                if zero_cnt < k:
                    zero_cnt += 1
                    one_cnt += 1
                    _max = max(_max,one_cnt)
                    right += 1
                else:
                    while left < right and nums[left]==1:
                        left += 1
                        one_cnt -= 1
                    if left < right and nums[left]==0:
                        left += 1
                        zero_cnt -= 1
                        one_cnt -= 1
        return _max
s = Solution()
print(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
print(s.longestOnes([0,0,1,1,1,0,0], k = 0))
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1], k = 0))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 0))


