from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visit = [False] * n
        r = [True] * n
        for res in restricted:
            r[res] = False
        dic = {i:[] for i in range(n)}
        for edge in edges:
            dic[edge[0]].append(edge[1])

            dic[edge[1]].append(edge[0])
        s = [0]
        count = 0
        while s:
            idx = s[-1]
            visit[idx] = True
            target = True
            for vex in dic[idx]:
                if not visit[vex] and r[vex]:
                    s.append(vex)
                    target = False
                    break
            if target:
                j = s.pop()
                count += 1
        return count
s = Solution()
s.reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5])