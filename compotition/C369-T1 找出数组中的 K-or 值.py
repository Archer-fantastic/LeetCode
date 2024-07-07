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