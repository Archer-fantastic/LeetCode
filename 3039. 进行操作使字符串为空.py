import collections


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        dic = collections.Counter(s)
        num = max(dic.values())
        l = list(s)
        for idx in range(len(l)-1,-1,-1):
            ch = l[idx]
            l[idx] = dic[ch]
            dic[ch] -= 1
        ans = ""
        for idx in range(len(l)):
            if l[idx] == num:
                ans += s[idx]
        return ans
s =Solution()
s.lastNonEmptyString(s = "aabcbbca")
s.lastNonEmptyString(s = "aabcbbca")
s.lastNonEmptyString(s = "abcd")