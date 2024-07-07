from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        def sort(i,j):
            for k in range(min(m-i,n-j)):
                ii = i
                jj = j
                while ii+1 < m and jj+1 < n:
                    if mat[ii][jj] > mat[ii+1][jj+1]:
                        mat[ii][jj] , mat[ii + 1][jj + 1] = mat[ii+1][jj+1] , mat[ii][jj]
                    ii += 1
                    jj += 1
            display()
        def display():
            for x in range(m):
                for y in range(n):
                    print(mat[x][y],end="\t")
                print()
            print()
        # display()
        for i in range(n):
            sort(0,i)
        for i in range(m):
            sort(i,0)
        return mat
s = Solution()
print(s.diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print(s.diagonalSort(mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))