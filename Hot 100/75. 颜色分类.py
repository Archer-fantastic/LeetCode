from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = 0
        k = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                i += 1
            elif nums[idx] == 1:
                k += 1
            else:
                j += 1
        for idx in range(len(nums)):
            if idx < i:
                nums[idx] = 0
            elif idx < i+j:
                nums[idx] = 1
            else:
                nums[idx] = 2

        print(nums)

    def sortColors2(self, nums: List[int]) -> None:
        i = 0
        j = len(nums) - 1
        idx = 0
        while idx < j:
            if nums[idx] == 0:
                nums[i] = 0
                if idx != i:
                    nums[idx] = 1
                i += 1
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums[idx] = nums[j]
                nums[j] = 2
                j -= 1
        print(nums)
s = Solution()
s.sortColors2([2,0,2,1,1,0])
s.sortColors2([1,0,2])