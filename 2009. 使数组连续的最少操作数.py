from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        nums.sort()
        # nums = list(set(nums))
        n = len(nums)
        _min = n
        s = set()
        i,j = 0,0
        while i<n:
            if i > 0 and nums[i-1]==nums[i]:
                continue
            if i > 0:
                s.remove(nums[i-1])
            while j<n and nums[j]<nums[i]+n:
                s.add(nums[j])
                j+=1
            _min = min(_min,n-len(s))
            i+=1
        return _min
s = Solution()
print(s.minOperations([4,2,5,3]))
print(s.minOperations([1,2,3,5,6]))
print(s.minOperations([1,10,100,1000]))
