import time


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        count_dic = {}
        for idx, num in enumerate(nums):
            if num not in count_dic:
                count_dic[num] = 1
            elif count_dic[num] < 3:
                count_dic[num] += 1
        _nums = []
        for num in count_dic:
            for i in range(count_dic[num]):
                _nums.append(num)
        _nums = sorted(_nums)
        _len = len(_nums)
        _min_val = 0xFFFFFFF
        ans = ""
        if target > 3000:
            return _nums[-1] + _nums[-2] + _nums[-3]
        elif target < -3000:
            return _nums[0] + _nums[1] + _nums[2]
        for i in range(_len):
            for j in range(i + 1, _len):
                for k in range(j + 1, _len):
                    num = abs(target - _nums[i] - _nums[j] - _nums[k])
                    if num < _min_val:
                        _min_val = num
                        ans = _nums[i] + _nums[j] + _nums[k]
        return ans