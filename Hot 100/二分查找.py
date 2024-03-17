from typing import List


class Solution(object):
    # 35. 搜索插入位置
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    # 74. 搜索二维矩阵
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        m = len(matrix)
        n = len(matrix[0])
        _max = matrix[-1][-1]
        _min = matrix[0][0]
        if _min <= target <= _max:
            for i in range(m):
                if bin_search(matrix[i],target):
                    return True
        return False

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def r():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r if nums[r] == target else -1
        def l():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l if nums[l] == target else -1

        if len(nums) == 0: return [-1,-1]
        return [l(),r()]

    # 33. 搜索旋转排序数组
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            elif nums[mid] > nums[l]:
                # 左边有序，右边无序
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 左边无序，右边有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return l if nums[l] == target else -1
    # 153. 寻找旋转排序数组中的最小值
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        _min = 10 ** 4
        while l <= r:
            mid = (l + r) // 2
            # _min = min(_min,nums[l],nums[mid],nums[r])
            if nums[mid] >= nums[l]:
                # 左边有序，右边无序
                _min = min(_min,nums[l])
                l = mid + 1
            else:
                # 左边无序，右边有序
                _min = min(_min,nums[mid])
                r = mid - 1
        return _min
s = Solution()
print(s.findMin([3,1,2]))
print(s.findMin([3,4,5,1,2]))
# print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11,13,15,17]))