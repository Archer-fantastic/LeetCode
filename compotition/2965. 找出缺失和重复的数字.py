import collections
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dic = {i:0 for i in range(1,n**2+1)}
        for i in range(n):
            for j in range(n):
                dic[grid[i][j]]+=1
        for d in dic:
            if dic[d] == 2:
                a = d
            elif dic[d] == 0:
                b = d
        return [a,b]
s = Solution()
print(s.findMissingAndRepeatedValues([[1,3],[2,2]]))
print(s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))