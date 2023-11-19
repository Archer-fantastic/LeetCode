class Solution(object):
    def __init__(self):
        self.arr = {}

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n in self.arr:
            return self.arr[n]
        if n <= 2:
            if n == 2:
                self.arr[n] = x * x
            if n == 1:
                self.arr[n] = x
            if n == 0:
                self.arr[n] = 1
            return self.arr[n]

        if n & (n-1) == 0:
            self.arr[n] = self.myPow(x,n // 2) * self.myPow(x,n // 2)
        else:
            self.arr[n] = self.myPow(x,n - (n & (n-1))) * self.myPow(x,n & (n-1))
        return self.arr[n]
    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n in self.arr:
            return self.arr[n]
        if n <= 1:
            self.arr[n] = x if n == 1 else 1
            return self.arr[n]

        if n & (n-1) == 0:
            self.arr[n] = self.myPow(x,n // 2) * self.myPow(x,n // 2)
        else:
            self.arr[n] = self.myPow(x,n - (n & (n-1))) * self.myPow(x,n & (n-1))
        return self.arr[n]
