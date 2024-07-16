class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        taget = True
        num = 0
        for i in range(k):
            if num == n-1 :
                taget = False
            if num == 0:
                taget = True
            if taget:
                num += 1
            else:
                num -= 1
        return num
s = Solution()
s.numberOfChild(n = 3, k = 5)
s.numberOfChild(n = 5, k = 6)
s.numberOfChild(n = 4, k = 2)

