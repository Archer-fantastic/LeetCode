from typing import List
from collections import Counter
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # 计算两点之间的距离，因为是找距离相等的点，所以不开根号也可以
        def d(A,B):
            return (A[0]-B[0])**2 + (A[1]-B[1])**2
        # 本题的思路就是 记录下每个点到其余各点的距离 若有等距离的两个点就构成了一个回旋镖
        n = len(points)
        ans = 0
        for i in range(n):
            c = Counter()
            for j in range(n):
                if i == j:
                    continue
                c[d(points[i],points[j])] += 1

            for num in c:
               ans += c[num]*(c[num]-1)
        return ans
s= Solution()
print(s.numberOfBoomerangs(points = [[0,0],[1,0],[2,0]]))
