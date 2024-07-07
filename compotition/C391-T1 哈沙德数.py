class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        xx = x
        while x!=0:
            s += x% 10
            x //= 10
        return s if xx % s ==0 else -1