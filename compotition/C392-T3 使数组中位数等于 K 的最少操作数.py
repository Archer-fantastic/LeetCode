from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n//2]
        idx = n // 2
        c = 0
        # print(nums,idx)
        # print("mid:",mid)
        if k == mid:
            return c
        elif k > mid:
            c += (k-mid)
            for i in range(idx+1,n):
                if nums[i] < k:
                    c += (k - nums[i])
                else:
                    break
        else:
            c += abs(k-mid)
            for i in range(idx-1,-1,-1):
                if nums[i] > k:
                    c += (nums[i] - k)
                else:
                    break
        return c

s = Solution()
# print(s.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 4))
# print(s.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 7))
# print(s.minOperationsToMakeMedianK(nums = [1,2,3,4,5,6], k = 4))
print(s.minOperationsToMakeMedianK([2,68,15,39,30,39,97,68],2))