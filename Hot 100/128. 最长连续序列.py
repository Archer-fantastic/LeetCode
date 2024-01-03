from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for idx,num in enumerate(nums):
            dic[num] = idx
        max_len = 0
        for key in dic:
            if key-1 in dic:
                continue
            else:
                cur_len = 1
                k = key + 1
                while k in dic:
                    k += 1
                    cur_len += 1
            max_len = max(cur_len,max_len)
        return max_len
    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = nums.sort()

        i = 1
        n = len(nums)
        cur_len = 1
        max_len = 1
        while i < n:
            if nums[i-1] == nums[i] - 1:
                i += 1
                cur_len += 1
            else:
                max_len = max(cur_len,max_len)
                cur_len = 1


s = Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))