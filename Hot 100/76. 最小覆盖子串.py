from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        left = 0
        n = len(s)
        cn1 = Counter()
        cn2 = Counter(t)
        min_len = 0xFFFFF
        cur_len = 0
        def judge():
            for c in cn2:
                if cn2[c] > cn1[c]:
                    return False
            return True
        ans = ""
        for i in range(n):
            cn1[s[i]] += 1
            cur_len += 1
            while judge():
                if cur_len < min_len:
                    min_len = cur_len
                    ans = s[left:i+1]
                cn1[s[left]] -= 1
                left += 1
                cur_len -= 1
        return ans
s = Solution()
# print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))
# print(s.minWindow(s = "a", t = "a"))
# print(s.minWindow( s = "a", t = "aa"))
print(s.minWindow( s = "cabwefgewcwaefgcf", t = "cae"))

