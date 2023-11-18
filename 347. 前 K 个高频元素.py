from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        nums = list(zip(dic.keys(), dic.values()))
        nums.sort(key=lambda x: -x[1])
        return [nums[i][0] for i in range(k)]
    

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(s.topKFrequent(nums = [1], k = 1))
print(s.topKFrequent(nums = [1], k = 1))