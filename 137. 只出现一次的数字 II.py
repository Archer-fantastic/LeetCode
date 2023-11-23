class Solution(object):
    def singleNumber(self, nums):
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        for num in dic:
            if dic[num]==1:
                return num