from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur_ones = 0
        n= len(nums)
        _max = 0
        T = True
        left = 0
        right = 0
        while right<n:
            if nums[right] == 1:
                cur_ones += 1
            elif T:
                T = False
                # cur_ones += 1
            else:
                while nums[left] == 1:
                    left += 1
                    cur_ones -= 1
                left += 1
                T = True
                continue
            right += 1
            _max = max(_max,cur_ones)
        return min(_max,n-1)

s = Solution()
# print(s.longestSubarray([1,1,0,0,1,1,1,0,1]))
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))