from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        a,b = n,-1
        c,d = m,-1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    a = min(a,i)
                    b = max(b,i)
                    c = min(c,j)
                    d = max(d,j)
        return (b-a+1)*(d-c+1)
s = Solution()
s.minimumArea(grid = [[0,1,0],[1,0,1]])
s.minimumArea(grid = [[0,0],[1,0]])

