from typing import List


class Solution:
    def m(self,num):
        _max = 0
        while num > 0:
            _max = max(_max,num%10)
            num //= 10
        return _max
    def maxSum(self, nums: List[int]) -> int:
        m = [self.m(num) for num in nums]
        mm = list(zip(nums,m))
        mm = sorted(mm,key=lambda x:x[1])
        # print(mm)

        ans = -1
        _l = [[] for i in range(len(set(m)))]
        _l[0].append(mm[0][0])
        n = mm[0][1]
        idx = 0
        for mmm in mm[1:]:
            if mmm[1]!=n:
                idx += 1
                n = mmm[1]
            _l[idx].append(mmm[0])
        print(_l)
        for ll in _l:
            if len(ll) >= 2:
                ll = sorted(ll)
                ans = max(ans,ll[-1]+ll[-2])
        return ans

s = Solution()
# print(s.maxSum([51,71,17,24,42]))
print(s.maxSum([84,91,18,59,27,9,81,33,17,58]))

