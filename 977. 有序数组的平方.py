from typing import List


class Solution:
    def sortedSquares3(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        return [num**2 for num in sorted(nums,key=lambda x:abs(x))]
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        l1,r1 = 0,len(nums)-1
        r2 = len(nums)-1
        arr = [0] * len(nums)
        while l1 <= r1:
            if abs(nums[l1]) < abs(nums[r1]):
                arr[r2] = abs(nums[r1])
                r1 -= 1
            else:
                arr[r2] = abs(nums[l1])
                l1 += 1
            r2 -= 1
        return [num**2 for num in arr]
s = Solution()
print(s.sortedSquares2(nums = [-4,-1,0,3,10]))