from typing import List


class Solution:
    def sumIndicesWithKSetBits1(self, nums: List[int], k: int) -> int:
        def cal_count(idx):
            return str(bin(idx)).count("1")
        _sum = 0
        for idx, num in enumerate(nums):
            _sum += num if cal_count(idx) == k else 0
        return _sum
    def sumIndicesWithKSetBits2(self, nums: List[int], k: int) -> int:
        def cal_count(idx):
            count = 0
            while idx != 0:
                idx = idx & (idx-1)
                count+=1
            return count
        _sum = 0
        for idx, num in enumerate(nums):
            _sum += num if cal_count(idx) == k else 0
        return _sum
    def sumIndicesWithKSetBits3(self, nums: List[int], k: int) -> int:
        return sum(num if str(bin(idx)).count("1") == k else 0 for idx, num in enumerate(nums))
s = Solution()
print(s.sumIndicesWithKSetBits2(nums = [5,10,1,5,2], k = 1))
print(s.sumIndicesWithKSetBits2(nums = [4,3,2,1], k = 2))