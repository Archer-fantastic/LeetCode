class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        n = min(n1, min(n2, n3))
        _len = 0
        for i in range(n):
            if s1[i] == s2[i] == s3[i]:
                _len += 1
            else:
                break
        if _len == 0:
            return -1
        else:
            return n1 + n2 + n3 - 3 * _len
