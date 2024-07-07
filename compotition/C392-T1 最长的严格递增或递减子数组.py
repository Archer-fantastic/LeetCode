from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c1 = 1
        c2 = 1
        n = len(nums)

        for i in range(n):
            t = 1
            for j in range(i,n-1):
                if nums[j] < nums[j+1]:
                    t += 1
                else:
                    break
            c1 = max(c1,t)
        for i in range(n):
            t = 1
            for j in range(i,n-1):
                if nums[j] > nums[j+1]:
                    t += 1
                else:
                    break
            # print("t2:",t)
            c2 = max(c2,t)
        # print(c1,c2)
        return max(c1,c2)
s = Solution()
print(s.longestMonotonicSubarray([1,4,3,3,2]))