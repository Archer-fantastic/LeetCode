from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        happiness = sorted(happiness, reverse=True)
        for i in range(k):
            num = max(0, happiness[i] - i)
            ans += num
        return ans
