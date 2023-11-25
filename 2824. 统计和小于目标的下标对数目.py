from typing import List


class Solution:

    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        def bin_search(nums,target):
            n = len(nums)
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    while mid+1 < n and nums[mid+1] == target:
                        mid += 1
                    return mid
                elif nums[mid] < target:
                    left = mid +1
                else:
                    right = mid-1
            return left if left < n and nums[left] < target else left-1
        # for i in range(17):
        #     print(bin_search([2,5,6,8,10,12,14,16],i))
        # print(nums)
        ans = 0
        for idx,num in enumerate(nums):
            i = bin_search(nums,target-num-1)
            # print(num,target-num-1,i,i-idx)
            ans += max(0,i - idx)
            if i - idx < 0:
                break
        return ans
s = Solution()
# print(s.countPairs(nums = [-1,1,2,3,1,2,3,4,5,6,7,8,9,1,2,3,4,5], target = 6))
print(s.countPairs(nums = [6,-1,7,4,2,3], target = 8))
# print(s.countPairs(nums = [-1,1,2,3,1], target = 2))
print(s.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))
