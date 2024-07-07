from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        def check(i):
            for j in range(n):
                if i == j:
                    continue
                elif grid[i][j] == 1 and grid[j][i] == 0:
                    continue
                else:
                    return False
            return True
        n = len(grid)
        for i in range(n):
            if check(i):
                return i

s = Solution()
print(s.findChampion([[0,1],[0,0]]))
print(s.findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]]))
print(s.findChampion(grid = [[0,0,1,0],[1,0,1,0],[0,0,0,0],[1,1,1,0]]))