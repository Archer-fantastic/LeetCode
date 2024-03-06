
from typing import List
class Solution:
    # 2. 两数之和
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for idx,num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],idx]
            else:
                dic[num] = idx
        return [-1,-1]
    # 49. 字母异位词分组
    # 最基本的想法就是，用一个数组或者字典记录字母出现的个数，再分组，但是总感觉有些麻烦
    # 改进后的想法：把sort之后的字符串当做字典的key值
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            s = "".join(sorted(str))
            if s in dic:
                dic[s].append(str)
            else:
                dic[s] = [str]
        return list(dic.values())
s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
print(s.twoSum(nums = [3,2,4], target = 6))
print(s.twoSum(nums = [3,3], target = 6))