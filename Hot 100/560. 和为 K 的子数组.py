from typing import List

class Solution(object):
    def subarraySum(self, nums, k):
        arr = [0]
        for num in nums:
            arr.append(arr[-1] + num)
        dic = {0: 1}
        res = 0
        for num in arr[1:]:
            res += dic.get(num - k, 0)
            dic[num] = dic.get(num, 0) + 1
        return res
s = Solution()
print(s.subarraySum(nums = [1,1,1], k = 2))
print(s.subarraySum(nums = [1,2,3], k = 3))
print(s.subarraySum(nums = [1], k = 0))
print(s.subarraySum(nums = [-1,-1,1], k = 0))