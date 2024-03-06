from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0 for _ in range(32)]

        for num in nums:
            s = bin(num)[2:][::-1]
            for idx,ss in enumerate(s):
                if ss == "1":
                    cnt[idx] += 1
        ans = 0
        for idx,c in enumerate(cnt):
            if c >= k:
                ans += 2**idx
        return ans
s =Solution()
s.findKOr(nums = [7,12,9,8,9,15], k = 4)
s.findKOr(nums = [2,12,1,11,4,5], k = 6)