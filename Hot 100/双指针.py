from typing import List


class Solution(object):
    # 283. 移动零
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
    # 11. 乘最多水的容器
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    # 15. 三数之和
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 针对一些[-1,0,1]*50这种情况做了一些优化
        # 要想让三数之和为0，要么是3个0，要么是 正/负/0的混合，不可能会出现三正或者三负的情况
        # 也就是说[-1,0,1]*50 <==> [-1,-1,0,0,0,1,1]
        # 用字典计数做了一些优化
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        array = []
        for key in dic:
            if key == 0 and dic[key] > 2:
                array.extend([0,0,0])
            else:
                count = min(2,dic[key])
                array.extend([key]*count)
        array = sorted(array)
        # 双指针，主要是如何进行同时去重的问题
        ans = []
        n = len(array)
        for i in range(n):
            if array[i] > 0: break
            if i > 0 and array[i] == array[i-1]: continue
            j = i + 1
            k = n - 1
            while j < k:
                if array[i] + array[j] + array[k] == 0:
                    ans.append([array[i] , array[j] , array[k]])
                    k -= 1
                    j += 1
                    while j < k and array[k] == array[k + 1]: k -= 1
                    while j < k and array[j] == array[j - 1]: j += 1
                elif array[i] + array[j] + array[k] > 0:
                    k -= 1
                    while j < k and array[k] == array[k + 1]: k -= 1
                else:
                    j += 1
                    while j < k and array[j] == array[j - 1]: j += 1
        return ans

s = Solution()
s.moveZeroes2([0,1,0,3,12])
s.moveZeroes2([1])