from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _s = [1]
        _n = [1]
        for num in nums:
            _s.append(num*_s[-1])
        for num in nums[::-1]:
            _n.append(num*_n[-1])
        _s.append(1)
        _n.append(1)
        _n = _n[::-1]
        ans  = []
        for idx in range(1,len(nums)+1):
            ans.append(_s[idx-1]*_n[idx+1])
        return ans

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf(nums = [-1,1,0,-3,3]))