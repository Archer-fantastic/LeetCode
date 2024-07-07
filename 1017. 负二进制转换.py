class Solution:
    def baseNeg2(self, n: int) -> str:
        k = 1
        ans = []
        while n:
            if n % 2:
                ans.append('1')
                n -= k
            else:
                ans.append('0')
            n //= 2
            k *= -1
        return ''.join(ans[::-1]) or '0'


s = Solution()
print(s.baseNeg2(2))
print(s.baseNeg2(-4))
print(s.baseNeg2(100))