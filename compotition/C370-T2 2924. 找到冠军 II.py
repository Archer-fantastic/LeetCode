from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for i in range(n)]
        for edge in edges:
            indegree[edge[1]] += 1
        if indegree.count(0) > 1:
            return -1
        return indegree.index(0)
s = Solution()
print(s.findChampion(n = 3, edges = [[0,1],[1,2]]))
print(s.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]]))