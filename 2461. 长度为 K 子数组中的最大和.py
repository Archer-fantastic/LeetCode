from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        # for num in nums:
        #     pre.append(pre[-1]+num)
        _max = 0

        # print(pre)
        dic = {}
        for i in range(k):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for idx in range(k,len(nums)):
            if len(dic) == k:
                _max = max(_max,sum(dic.keys()))
            if nums[idx] in dic:
                dic[nums[idx]] += 1
            else:
                dic[nums[idx]] = 1
            dic[nums[idx-k]] -= 1
            if dic[nums[idx-k]] == 0:
                dic.pop(nums[idx-k])
        if len(dic) == k:
            _max = max(_max, sum(dic.keys()))
        return _max
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans, temp = 0, 0
        n = len(nums)
        hashmap = defaultdict(int)
        for i in range(k):
            temp += nums[i]
            hashmap[nums[i]] += 1
        if len(hashmap) == k:
            ans = temp
        for i in range(k, n):
            temp -= nums[i - k]
            hashmap[nums[i - k]] -= 1
            if hashmap[nums[i - k]] == 0:
                del hashmap[nums[i - k]]

            temp += nums[i]
            hashmap[nums[i]] += 1
            if len(hashmap) == k:
                ans = max(ans, temp)
        return ans

s = Solution()
print(s.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))
print(s.maximumSubarraySum(nums = [4,4,4], k = 3))
print(s.maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3))