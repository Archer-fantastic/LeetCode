from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        _sum = 0
        for i in range(n):
            if grumpy[i] == 0:
                _sum += customers[i]
                customers[i] = 0
        t = sum(customers[:minutes])
        _max = t
        for i in range(minutes,n):
            t = t + customers[i] - customers[i-minutes]
            _max = max(_max,t)
        return _sum + _max
s = Solution()
print(s.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))
print(s.maxSatisfied(customers = [1], grumpy = [0], minutes = 1))
