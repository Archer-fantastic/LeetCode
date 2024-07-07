from typing import List

# nums = [1,4,2,3,1,4], k = 3

'''
1 1 2 0 1 1
1 2
2 0
0 1
'''
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        print("--" * 50)
        print(nums)
        for idx in range(len(nums)):
            nums[idx] = nums[idx]%k
        _max = 0
        cnts = {}
        for i in range(k):
            cnt = nums.count(i)
            cnts[i] = cnt
            _max = max(_max,cnt)
        def fun(nums,a,b):
            aa = -1
            bb = -1
            res = 0
            for idx in range(len(nums)):
                if nums[idx] == a:
                    aa = 1
                    bb = 0
                    res+=1
                    i = idx
                    break
                elif nums[idx] == b:
                    a,b = b,a
                    aa = 1
                    bb = 0
                    res+=1
                    i = idx
                    break
            for idx in range(i+1,len(nums)):
                if aa == 0 and nums[idx]==a:
                    res += 1
                    aa = 1
                    bb = 0
                elif bb == 0 and nums[idx]==b:
                    res += 1
                    aa = 0
                    bb = 1
            return res
        dic = {}
        l = []
        for num in nums:
            if num not in l:
                l.append(num)
        for idx in range(len(l)-1):
            for j in range(idx+1,len(l)):
                if cnts[l[idx]] + cnts[l[j]] <= _max:
                    continue
                if (l[idx],l[j]) not in dic and (l[j],l[idx]) not in dic:
                    res = fun(nums,l[idx],l[j])
                    dic[(l[idx],l[j])] = res
                    _max = max(_max,res)
        print(nums)
        print(dic)

        return _max
s = Solution()
print(s.maximumLength(nums = [1,2,3,4],k=2))
print(s.maximumLength(nums = [1,2,1,1,2,1,2],k=2))
print(s.maximumLength(nums = [1,3],k=2))
print(s.maximumLength(nums = [1,5,9,4,2],k=2))
print(s.maximumLength(nums = [1,7,8,7,5],k=2))
print(s.maximumLength(nums = [1,4,2,3,1,4], k = 3))
print(s.maximumLength(nums = [1,2,3,4,5], k = 2))
print(s.maximumLength([2,6,6,7,3],k=3))
print(s.maximumLength([2,4,7,1,2,6,7],8))
print(s.maximumLength([4,4,5,8,5],4))

