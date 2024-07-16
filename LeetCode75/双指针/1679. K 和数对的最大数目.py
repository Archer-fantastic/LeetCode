from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right = 0,len(nums)-1
        # 1 1 2 2 3 3 4 4 5 5 6 6
        # while nums[right] >= k:
        #     right -= 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                ans += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return ans