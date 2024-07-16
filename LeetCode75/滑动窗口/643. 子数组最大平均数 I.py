from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        cur_sum = 0
        _max = 0
        for i in range(k):
            cur_sum += nums[i]
        _max = cur_sum/k
        for right in range(k,len(nums)):
            cur_sum-=nums[left]
            left += 1
            cur_sum+=nums[right]
            _max = max(_max,cur_sum/k)
        return _max
