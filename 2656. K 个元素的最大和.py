from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # 问题转化为：求[max,max+k-1]的累加和
        _max = max(nums)
        return sum([_max + i for i in range(k)])

    def maximizeSum(self, nums: List[int], k: int) -> int:
        return k * (2 * max(nums) + k - 1) // 2
