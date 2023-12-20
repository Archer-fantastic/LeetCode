from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        "1212 2"
        def judge(l,k):
            for idx,num in enumerate(l[k:] + l[:k]):
                if num != l[idx]:
                    return False
            return True
        m,n = len(mat),len(mat[0])
        k = k%n
        for _l in mat:
            # print(_l,judge(_l,k))
            if not judge(_l,k):
                return False
        return True

s= Solution()
print(s.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 3))
print(s.areSimilar(mat = [[2,2],[2,2]], k = 3))
print(s.areSimilar(mat = [[1,2]], k = 1))
print(s.areSimilar(mat = [[4,9,10,10],[9,3,8,4],[2,5,3,8],[6,1,10,4]], k = 5))
print(s.areSimilar(mat = [[5,4,5,10,5]], k = 9))