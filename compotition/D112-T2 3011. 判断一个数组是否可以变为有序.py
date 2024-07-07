from itertools import pairwise
from typing import List


class Solution:
    def ones(self,num):
        count = 0
        while num > 0:
            num = num & (num-1)
            count+=1
        return count
    def canSortArray(self, nums: List[int]) -> bool:
        n = []
        for num in nums:
            n.append(self.ones(num))
        m = list(zip(nums,n,range(len(nums))))
        # print(m)
        l = {i:[] for i in set(n)}
        ll = {i:[] for i in set(n)}
        for num,c,idx in m:
            l[c].append(num)
            ll[c].append(idx)
        for lll in l:
            l[lll] = sorted(l[lll])
        for lll in ll:
            ll[lll] = sorted(ll[lll])
        print(l)
        print(ll)
        for key in l:
            for idx,num in enumerate(l[key]):
                nums[ll[key][idx]] = num
        print(nums)
        for idx in range(len(nums)-1):
            if nums[idx] > nums[idx+1]:
                return False
        return True
    def canSortArray2(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            start = i
            ones = nums[i].bit_count()
            i += 1
            while i < n and nums[i].bit_count() == ones:
                i += 1
            nums[start:i] = sorted(nums[start:i])
        return all(x <= y for x, y in pairwise(nums))


s =Solution()
# print(s.canSortArray([8,4,2,30,15]))
# print(s.canSortArray([1,2,3,4,5]))
# print(s.canSortArray([3,16,8,4,2]))
print(s.canSortArray([75,34,30]))