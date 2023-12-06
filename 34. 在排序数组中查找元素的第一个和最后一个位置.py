from typing import List


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        def get_idx():
            if len(nums) == 0:
                return -1
            left,right = 0,len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        idx = get_idx()
        if idx == -1:
            return [-1,-1]
        idx1,idx2 = idx,idx
        while idx1-1 >= 0 and nums[idx1-1] == target:
            idx1 -= 1
        while idx2+1 < len(nums) and nums[idx2+1] == target:
            idx2 += 1
        return [idx1,idx2]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_right():
            l,r = 0,len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r if nums[r] == target else -1
        def get_left():
            l,r = 0,len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l if l<len(nums) and nums[l] == target else -1
        if len(nums) == 0: return [-1,-1]
        return [get_left(),get_right()]
s = Solution()
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(s.searchRange(nums = [2,2], target = 3))
print(s.searchRange(nums = [12 for i in range(20)], target = 12))
print(s.searchRange(nums = [], target = 12))

