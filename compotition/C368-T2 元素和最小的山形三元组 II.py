from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        left = [0,nums[0]]
        right = [nums[-1]]
        _min = nums[0]
        for idx in range(2,len(nums)-1):
            _min = min(_min,nums[idx-1])
            left.append(_min)
        _min = nums[-1]
        for idx in range(len(nums)-3,0,-1):
            _min = min(_min,nums[idx+1])
            right.insert(0,_min)
        _min = 0xFFFFFFFF
        right.insert(0,0)
        for i in range(1,len(nums)-1):
            if nums[i] > left[i] and nums[i] > right[i]:
                _min = min(_min,nums[i]+left[i]+right[i])
        return -1 if _min==0xFFFFFFFF else _min