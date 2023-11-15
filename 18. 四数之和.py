import copy
import time


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        count_dic = {}
        for idx, num in enumerate(nums):
            if num not in count_dic:
                count_dic[num] = 1
            elif count_dic[num] < 4:
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

        # print(_nums)
        # print(dic)

        ans = []
        _len = len(_nums)
        t = 0
        for i in range(_len):
            for j in range(i + 1, _len):
                for k in range(j+1,_len):
                    if (target-_nums[i] - _nums[j] - _nums[k]) in dic:
                        tmp = copy.deepcopy(dic[target-_nums[i] - _nums[j] - _nums[k]])
                        if i in tmp:
                            tmp.remove(i)
                        if j in tmp:
                            tmp.remove(j)
                        if k in tmp:
                            tmp.remove(k)
                        if len(tmp) > 0 and tmp[0] > k:
                            s22 = time.time()
                            _l = sorted([_nums[i], _nums[j],_nums[k], target-(_nums[i] + _nums[j] + _nums[k])])
                            if _l not in ans:
                                ans.append(_l)
        return ans