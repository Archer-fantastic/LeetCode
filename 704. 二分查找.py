class Solution(object):
    def search(self, nums, target):
        # 二分查找，左闭右闭
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return target
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def search(self, nums, target):
        # 二分查找，左闭右闭
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return target
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1
