import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = copy.deepcopy(matrix)
        matrix = [[x[i] for x in n[::-1]] for i in range(len(n))]
        print(matrix)
s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
