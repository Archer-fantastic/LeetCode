class Solution:
    def numSquares(self, n: int) -> int:
        l = []
        for i in range(0,101):
            l.append(i**2)
        idx = 100
        count = 0
        while n > 0:
            if l[idx] <= n:
                n-=l[idx]
                count += 1
                print(l[idx],end=" ")
            else:
                idx -=1
        print()
        return count
s = Solution()
print(s.numSquares(10))
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(9876))
