from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 剪枝
        _len1 = len(s1)
        _len2 = len(s2)
        if _len2 < _len1:
            return False
        # 字典初始化
        dic1 = {ss: 0 for ss in s1}
        dic2 = Counter(s1)

        # 固定窗口的滑动窗口，那么就先要填满第一个窗口
        left = 0
        for i in range(_len1-1):
            if s2[i] in dic1:
                dic1[s2[i]] += 1

        def judge(dic1, dic2):
            for k in dic1:
                if dic1[k] != dic2[k]:
                    return False
            return True
        # 滑动过程就加一个减一个即可
        for i in range(_len1-1, _len2):
            if i < _len2 and s2[i] in dic1:
                dic1[s2[i]] += 1
            if judge(dic1, dic2):
                return True
            if s2[left] in dic1:
                dic1[s2[left]] -= 1
            left += 1
        return False

s = Solution()
print(s.checkInclusion(s1 = "ab",s2 = "eidboooa"))
print(s.checkInclusion(s1 = "ab",s2 = "eidboaoo"))