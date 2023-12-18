from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0,0]
        for idx,n1 in enumerate(nums1):
            if n1 in nums2:
                ans[0] += 1
        for idx,n2 in enumerate(nums2):
            if n2 in nums1:
                ans[1] += 1
        return ans