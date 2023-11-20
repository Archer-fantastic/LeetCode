from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        print(pre)
        _max = pre[1]
        for i in range(len(pre)):
            for j in range(i+1,len(pre)):
                _max = max(pre[j]-pre[i],_max)
        return _max
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([1]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-1,-2]))
# print(s.maxSubArray([i for i in range(10 ** 4)]))
