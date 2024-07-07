class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(n+1):
            for j in range(n+1-i):
                k = n-i-j
                if i <= limit and j <= limit and 0 <= k <= limit:

                    ans += 1
        return ans