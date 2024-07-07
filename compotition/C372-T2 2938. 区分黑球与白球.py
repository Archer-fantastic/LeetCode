class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        left = 0
        right = len(s) - 1
        while left < len(s) and s[left] == "0":
            left += 1
        while right >= 0 and s[right] == "1":
            right -= 1
        ans = 0
        idx = right
        while idx >= left:
            if s[idx] == "1":
                ans += (right - idx)
                idx -= 1
                right -= 1
            else:
                idx -= 1
        return ans

