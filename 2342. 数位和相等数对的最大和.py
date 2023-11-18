from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 给定num，计算出num的数位和
        def fun(num):
            _sum = 0
            while num > 0:
                _sum += num%10
                num //= 10
            return _sum
        # 给定一个数组l，返回最大的两个数字之和
        def get_max_and_sec(l):
            _max = max(l)
            idx = l.index(_max)
            _sec = max(l[:idx] + l[idx+1:])
            return _max + _sec
        # step1：初始化一个字典 key是数位和，val是num {9: [18, 36], 7: [43, 7], 4: [13]}
        dic = {}
        for num in nums:
            tmp = fun(num)
            if tmp not in dic:
                dic[tmp] = [num]
            else:
                dic[tmp].append(num)
        print(dic)
        # step2：对于dic中每一个长度大于2的数组，与当前ans做max比较即可
        ans = -1
        for key in dic:
            if len(dic[key]) >= 2:
                ans = max(get_max_and_sec(dic[key]),ans)
        return ans

s = Solution()
print(s.maximumSum([18,43,36,13,7]))
print(s.maximumSum([10,12,19,14]))