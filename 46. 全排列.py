class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        ans = []
        for idx,num in enumerate(nums):
            tmp = nums[idx]
            nums[idx] = nums[0]
            nums[0] = tmp
            nums1 = self.permute(nums[1:])
            for idx,n in enumerate(nums1):
                nums1[idx].insert(0,nums[0])
            ans.extend(nums1)
        return ans