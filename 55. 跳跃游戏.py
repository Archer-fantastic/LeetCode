class Solution(object):
    def canJump(self, nums):
        k=0
        for i in range(len(nums)):
            if i>k:
                return False
            k = max(k,i+nums[i])
        return True