from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        self.ans = 0

        def dfs(i,j,depth):
            self.ans = max(self.ans,depth)
            for k in i,i-1,i+1:
                if j+1 < n and 0 <= k < m and grid[k][j+1] > grid[i][j]:
                    dfs(k,j+1,depth+1)
            return

        for i in range(m):
            dfs(i,0,0)
        return self.ans
s = Solution()
print(s.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
print(s.maxMoves(grid = [[3,2,4],[2,1,9],[1,1,7]]))
