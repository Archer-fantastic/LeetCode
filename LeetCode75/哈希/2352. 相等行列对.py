from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        a = [list(grid[i]) for i in range(m)]
        b = [list([grid[i][j] for i in range(m)]) for j in range(n)]
        print(a)
        print(b)
        ans = 0
        for i in range(m):
            for j in range(n):
                T = True
                for k in range(len(a[i])):
                    if a[i][k] != b[j][k]:
                        T = False
                        break
                if T: ans += 1
        return ans

s = Solution()
print(s.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))
print(s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
