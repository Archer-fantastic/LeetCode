class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            _s = "".join(sorted(s))
            if _s not in dic:
                dic[_s] = [s]
            else:
                dic[_s].append(s)
        return list(dic.values())