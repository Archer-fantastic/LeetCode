from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def fun(mat,j):
            l = []
            m,n = len(mat),len(mat[0])
            # 右
            for i in range(j,n-j):
                l.append(mat[j][i])
            # 判断是否是最中间那一行
            if m % 2 == 1 and j == (m+1)//2 - 1:
                return l
            # 下
            for i in range(j+1,m-j):
                l.append(mat[i][n-1-j])
            # 判断是否是最中间那一列
            if n % 2 ==1 and j == (n+1)//2 - 1:
                return l
            # 左
            for i in range(n-2-j,j-1,-1):
                l.append(mat[m-1-j][i])
            # 上
            for i in range(m-2-j,j,-1):
                l.append(mat[i][j])
            return l

        ans = []
        m, n = len(matrix), len(matrix[0])
        for i in range(min((m+1)//2,(n+1)//2)):
            ans.extend(fun(matrix,i))
        return ans
s = Solution()
print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder(matrix = [[1,2,3],[10,11,4],[9,12,5],[8,7,6]]))
print(s.spiralOrder(matrix = [[3],[2]]))
print(s.spiralOrder(matrix = [[6,9,7]]))