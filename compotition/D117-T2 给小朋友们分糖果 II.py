class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for a in range(min(n, limit) + 1):
            lo = max(0, n - a - limit)
            hi = min(n - a, limit)
            if hi >= lo:
                ans += hi - lo + 1
        return ans