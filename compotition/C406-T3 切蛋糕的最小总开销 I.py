from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        if m == 1:
            return sum(verticalCut)
        elif n == 1:
            return sum(horizontalCut)
        max_cost_1 = -1
        idx = -1
        for i,h in enumerate(horizontalCut):
            if h > max_cost_1:
                idx = i
                max_cost_1 = h
        max_cost_2 = -1
        idx2 = -1
        for i,v in enumerate(verticalCut):
            if v > max_cost_2:
                idx2 = i
                max_cost_2 = v
        if max_cost_1 >= max_cost_2:
            if idx+1 > len(horizontalCut)-1:
                return max_cost_1 + self.minimumCost(idx+1,n,horizontalCut[:idx],verticalCut)+ self.minimumCost(1,n,[],verticalCut)
            return max_cost_1 + self.minimumCost(idx+1,n,horizontalCut[:idx],verticalCut)+ self.minimumCost(m-idx-1,n,horizontalCut[idx+1:],verticalCut)
        else:
            if idx2+1 > len(verticalCut)-1:
                return max_cost_2 + self.minimumCost(m,idx2+1,horizontalCut,verticalCut[:idx2]) + self.minimumCost(m,1,horizontalCut,[])
            return max_cost_2 + self.minimumCost(m,idx2+1,horizontalCut,verticalCut[:idx2]) + self.minimumCost(m,n-idx2-1,horizontalCut,verticalCut[idx2+1:])
s = Solution()
# print(s.minimumCost(m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]))
# print(s.minimumCost(m = 2, n = 2, horizontalCut = [7], verticalCut = [4]))
print(s.minimumCost(m = 6, n = 3, horizontalCut = [2,3,2,3,1], verticalCut = [1,2]))
