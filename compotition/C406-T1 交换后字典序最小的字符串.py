import math


class Solution:
    def getSmallestString(self, s: str) -> str:

        n = len(s)
        _min = int(s)
        ans = s
        for i in range(n-1):
            if (int(s[i]) + int(s[i+1]))%2 == 0:
                tmp = s[:i] + s[i+1] + s[i]
                if i+2 < n:
                    tmp += s[i+2:]
                if int(tmp) < _min:
                    _min = int(tmp)
                    ans = tmp
        return ans
s = Solution()
print(s.getSmallestString("45320"))