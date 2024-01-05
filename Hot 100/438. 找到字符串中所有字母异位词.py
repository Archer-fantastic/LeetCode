import collections
from typing import List, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(p)
        n2 = len(s)
        pp = collections.Counter(p)
        ss = collections.Counter(s[:n1-1])
        left = 0
        ans = []
        for i in range(n1-1,n2):
            ss[s[i]] += 1
            if ss == pp:
                ans.append(left)
            ss[s[left]] -= 1
            if ss[s[left]] == 0: ss.pop(s[left])
            left += 1
        return ans
s = Solution()
print(s.findAnagrams(s = "cbaebabacd", p = "abc"))
print(s.findAnagrams(s = "abab", p = "ababc"))