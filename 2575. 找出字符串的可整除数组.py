from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # word = "998244353", m = 3
        n = len(word)
        ans = [0 for _ in range(n)]
        t = 0
        for i in range(n):
            t = t*10 + int(word[i])
            if t % m == 0:
                ans[i] = 1
            t = t % m
        return ans
s = Solution()
print(s.divisibilityArray(word = "998244353", m = 3))
print(s.divisibilityArray(word = "1010", m = 10))





