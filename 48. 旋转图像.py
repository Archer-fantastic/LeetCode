import copy


class Solution(object):
    def rotate(self, matrix):
        new_matrix = copy.deepcopy(matrix)
        for j in range(len(new_matrix)):
            matrix[j] = [i[j] for i in new_matrix][::-1]