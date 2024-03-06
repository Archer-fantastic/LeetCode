from typing import List


class Solution(object):
    # 70. 爬楼梯
    def __init__(self):
        self.s = {}
    def climbStairs(self, n: int) -> int:
        if n in self.s:
            return self.s[n]
        if n == 1 or n == 2:
            ans = n
        else:
            ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.s[n] = ans
        return self.s[n]
    # 118. 杨辉三角

    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(1, 1 + numRows):
            # [0,0]
            l = []
            for j in range(i + 1):
                if j - 1 < 0:
                    l.append(arr[i - 1][j])
                elif j >= i:
                    l.append(arr[i - 1][j - 1])
                else:
                    l.append(arr[i - 1][j - 1] + arr[i - 1][j])
            arr.append(l)
        print(arr)