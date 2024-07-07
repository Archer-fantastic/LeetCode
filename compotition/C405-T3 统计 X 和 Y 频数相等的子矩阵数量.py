from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        NUM = 2*10**6
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "X":
                    grid[i][j] = -1
                elif grid[i][j] == "Y":
                    grid[i][j] = 1
                else:
                    grid[i][j] = NUM
        pre = []
        for i in range(n):
            tmp = [grid[i][0]]
            for j in range(1,m):
                tmp.append(tmp[-1] + grid[i][j])
            pre.append(tmp)


        # for i in range(n):
        #     for j in range(m):
        #         print(grid[i][j],end=" ")
        #     print()
        # print(pre)
        pre2 = []
        for i in range(n):
            if i == 0:
                pre2.append(pre[0])
            else:
                tmp = []
                for j in range(m):
                    tmp.append(pre2[i-1][j] + pre[i][j])
                pre2.append(tmp)
        # print(pre2)

        ans = 0
        for i in range(n):
            for j in range(m):
                res = pre2[i][j]
                if res % NUM == 0 and res != NUM*(i+1)*(j+1):
                    ans += 1
        return ans
s = Solution()
print(s.numberOfSubmatrices(grid = [["X","Y","."],["Y",".","."]]))
print(s.numberOfSubmatrices(grid = [["X","X"],["X","Y"]]))
print(s.numberOfSubmatrices(grid = [["X","X"],["X","Y"]]))
print(s.numberOfSubmatrices( grid = [[".","."],[".","."]]))



