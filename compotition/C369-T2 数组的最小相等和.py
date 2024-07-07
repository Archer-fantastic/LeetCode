from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zero_count1 = nums1.count(0)
        zero_count2 = nums2.count(0)
        if sum1 >= sum2:
            max_sum = sum1
            min_sum = sum2
            max_zero = zero_count1
            min_zero = zero_count2
        else:
            max_sum = sum2
            min_sum = sum1
            max_zero = zero_count2
            min_zero = zero_count1

        if max_zero!=0 and min_zero!=0:
            if max_sum == min_sum:
                return max_sum + max(max_zero, min_zero)
            return max(max_sum+max_zero,min_zero+min_sum)
        if min_zero + max_zero == 0:
            return -1 if max_sum!=min_sum else max_sum

        if max_zero == 0:
            return max_sum if min_sum+min_zero <= max_sum else -1
        elif min_zero == 0:
            return -1