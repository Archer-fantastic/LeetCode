
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for idx,num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],idx]
            else:
                dic[num] = idx
        return [-1,-1]
s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
print(s.twoSum(nums = [3,2,4], target = 6))
print(s.twoSum(nums = [3,3], target = 6))