from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def judge(arr):
            if len(arr) == 0:
                return True
            num = arr[0]
            for i in arr[1:]:
                if num >= i:
                    return False
                num = i
            return True
        # print(judge([3,5,5]))
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n+1):
                if judge(nums[:i] + nums[j:]):
                    print(nums[:i] + nums[j:])
                    ans += 1
        return ans
s = Solution()
print(s.incremovableSubarrayCount([3,5,3,5]))
# print(s.incremovableSubarrayCount(nums = [6,5,7,8]))