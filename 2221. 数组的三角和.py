from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        _list = nums
        for i in range(n-1):
            _tmp = []
            for j in range(1,len(_list)):
                _tmp.append((_list[j]+_list[j-1]) % 10)
            _list = _tmp
            print(_list)
        return _list[0]
s = Solution()
print(s.triangularSum([1,2,3,4,5]))