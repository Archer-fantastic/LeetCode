from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dic = {mat[i][j]:(i,j) for j in range(n) for i in range(m)}
        c1 = [0]*m
        c2 = [0]*n
        for idx,num in enumerate(arr):
            i,j = dic[num]
            c1[i],c2[j]=c1[i]+1,c2[j]+1
            if c1[i] == n or c2[j] == m: return idx
s = Solution()
# print(s.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
# print(s.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))
print(s.firstCompleteIndex(arr = [1,4,5,2,6,3], mat = [[4,3,5],[1,2,6]]))
print(s.firstCompleteIndex(arr = [1,4,5,2,6,3], mat = [[4,3,5],[1,2,6]]))

