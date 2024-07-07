class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        def judge(x,y):
            return abs(x-y) <= min(x,y)
        n = len(nums)
        _max = 0
        for i in range(n):
            for j in range(i+1,n):
                if judge(nums[i],nums[j]):
                    _max = max(_max,nums[i]^nums[j])
        return _max