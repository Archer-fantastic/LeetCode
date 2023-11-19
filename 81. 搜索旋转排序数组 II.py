class Solution(object):
    def search(self, nums, target):
        if len(nums) <= 0:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target or nums[r] == target or nums[l] == target:
                return True
            elif nums[mid] == nums[l]:
                if sum(nums[l:mid+1]) / (1.0 * (mid + 1 - l)) == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[l]:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return True if 0 <= l <= len(nums) - 1 and nums[l] == target else False