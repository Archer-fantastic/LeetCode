import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        for key in dic:
            if dic[key] > 1:
                return key
s = Solution()
print(s.findDuplicate(nums = [1,3,4,2,2]))