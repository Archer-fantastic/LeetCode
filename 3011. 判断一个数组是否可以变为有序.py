from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def cal_cnt(num):
            cnt = 0
            while num > 0:
                num = (num & (num-1))
                cnt += 1
            return cnt
        dic = {}
        for i,num in enumerate(nums):
            cnt = cal_cnt(num)
            if cnt not in dic:
                dic[cnt] = [[i],[num]]
            else:
                dic[cnt][0].append(i)
                dic[cnt][1].append(num)
        print(dic)
        for item in dic:
            _l = sorted(dic[item][1])
            


            for i,num in enumerate(_l):
                nums[dic[item][0][i]] = num
        print(nums)

s = Solution()
print(s.canSortArray(nums = [8,4,2,30,15]))