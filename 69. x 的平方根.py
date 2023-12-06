class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l,r = 0,x
        while l < r:
            mid = l + (r-l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid
        return l-1
s = Solution()
for i in range(1,20):
    print(i,s.mySqrt(i))
print(s.mySqrt(12341212 ** 2 + 12))