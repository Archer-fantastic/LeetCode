class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+indexDifference,len(nums)):
                if abs(nums[j]-nums[i])>=valueDifference:
                    return [i,j]
        return [-1,-1]