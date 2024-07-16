class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for i,tt in enumerate(t):
            if tt == s[idx]:
                idx += 1
                if idx >= len(s):
                    return True
        return False

