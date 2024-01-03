from typing import List


class Solution:
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
print(s.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams(strs = [""]))
print(s.groupAnagrams(strs = ["a"]))