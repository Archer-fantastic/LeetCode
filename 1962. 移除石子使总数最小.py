import collections
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = [0 for _ in range(10**4+1)]
        for pile in piles:
            stones[pile] += 1
        _max = max(piles)
        while k > 0 :
            idx = _max
            while stones[idx] == 0:
                idx -= 1
            _max = idx
            stones[idx] -= 1
            stones[(idx+1)//2] += 1
            k -= 1
        ans = 0
        for i in range(len(stones)):
            ans += i*stones[i]
        return ans
    def minStoneSum2(self, piles: List[int], k: int) -> int:
        dic = collections.Counter(sorted(piles))
        idx = max(piles)
        while k > 0 :
            dic[idx] -= 1
            dic[(idx+1)//2] += 1
            if dic[idx] == 0:
                dic.pop(idx)
            idx = max(dic.keys())
            k -= 1

        ans = 0
        for d in dic:
            ans += d*dic[d]
        # for a,b in zip(dic.keys(),dic.values()):
        #     ans += a*b
        return ans

s = Solution()
print(s.minStoneSum2(piles = [1], k = 10000))
print(s.minStoneSum2(piles = [5,4,9], k = 2))
print(s.minStoneSum2(piles = [4,3,6,7], k = 3))