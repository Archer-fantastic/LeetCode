import copy
import time


class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        count_dic = {}
        for idx, num in enumerate(nums):
            if num not in count_dic:
                count_dic[num] = 1
            elif count_dic[num] < 3 and num == 0:
                count_dic[num] += 1
            elif count_dic[num] < 2:
                count_dic[num] += 1
        _nums = []
        _nums_idx = 0
        dic = {}
        for num in count_dic:
            for i in range(count_dic[num]):
                _nums.append(num)
                if num not in dic:
                    dic[num] = [_nums_idx]
                else:
                    dic[num].append(_nums_idx)
                _nums_idx += 1

        ans = []
        _len = len(_nums)
        t = 0
        for i in range(_len):
            for j in range(i + 1, _len):
                if -(_nums[i] + _nums[j]) in dic:
                    tmp = copy.deepcopy(dic[-(_nums[i] + _nums[j])])
                    if i in tmp:
                        tmp.remove(i)
                    if j in tmp:
                        tmp.remove(j)
                    if len(tmp) > 0 and tmp[0] > j:
                        _l = sorted([_nums[i], _nums[j], -(_nums[i] + _nums[j])])
                        if _l not in ans:
                            ans.append(_l)
        return ans