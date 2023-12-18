from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def judge(var,target):
            a,b,c,m = var[0],var[1],var[2],var[3]
            return ((a**b % 10)**c)%m == target
        n = len(variables)
        res = []
        for i in range(n):
            if judge(variables[i],target):
                res.append(i)
        return res
s = Solution()
print(s.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2))
print(s.getGoodIndices(variables = [[39,3,1000,1000]], target = 17))
