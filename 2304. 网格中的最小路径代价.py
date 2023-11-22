from typing import List

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        self.min_cost = 0xFFFFFFFF
        m,n = len(grid),len(grid[0])
        def dfs(i,cost):
            if i < m:
                for j in range(n):
                    cost += grid[i][j]
                    cost += moveCost[grid[i][j]][j]
                    if cost < self.min_cost:
                        dfs(i+1,cost)
                    else:
                        return
                    cost -= moveCost[grid[i-1][j]][j]
                    cost -= grid[i][j]
            else:
                self.min_cost = min(self.min_cost,cost)
                # print()
                print(self.min_cost)
                # print()
        for num in grid[-1]:
            for j in range(n):
                moveCost[num][j] = 0
        cost = 0
        dfs(0,cost)
        print(self.min_cost)
s = Solution()
s.minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])