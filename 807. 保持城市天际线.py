from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        row = [max(grid[i]) for i in range(m)]
        col = [max([grid[j][i] for j in range(m)]) for i in range(n)]
        for i in range(m):
            for j in range(n):
                ans += min(row[i],col[j])-grid[i][j]
        return ans
s = Solution()
s.maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])

