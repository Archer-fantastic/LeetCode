from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def judge(a,b):
            l = len(a)
            if len(b) >= l and a==b[:l] and a==b[-l:]:
                return True
            return False
        l = len(words)
        c = 0
        for i in range(l):
            for j in range(i+1,l):
                if judge(words[i],words[j]):
                    c+=1
        return c
s = Solution()
print(s.countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(s.countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(s.countPrefixSuffixPairs(words = ["abab","ab"]))
