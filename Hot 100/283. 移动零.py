class Solution(object):
    def moveZeroes(self, nums):
        low = 0
        n = len(nums)
        for fast in range(n):
            if nums[fast] != 0:
                nums[low] = nums[fast]
                if fast != low:
                    nums[fast] = 0
                low += 1
    def moveZeroes2(self, nums):
        low = 0
        n = len(nums)
        for fast in range(n):
            if nums[fast] != 0:
                nums[low] = nums[fast]
                low += 1
        for idx in range(low,n):
            nums[idx] = 0

        print(nums)
s = Solution()
s.moveZeroes2([0,1,0,3,12])
s.moveZeroes2([1])