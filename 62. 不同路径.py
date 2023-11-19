class Solution(object):
    def fac(self,fac,m):
        if m == 1 or m == 0:
            return 1
        if fac[m] >0:
            return fac[m]
        fac[m] = self.fac(fac,m-1) * m
        return fac[m]
    def uniquePaths(self, m, n):
        fac = [-1 for _ in range(201)]
        num1 = self.fac(fac,m+n-2)
        num2 = self.fac(fac,m-1)
        num3 = self.fac(fac,n-1)
        return int(num1 / (num2 * num3))

    def fac(self, m):
        if m == 1 or m == 0:
            return 1
        return self.fac(m - 1) * m

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(self.fac(m + n - 2) / (self.fac(m - 1) * self.fac(n - 1)))