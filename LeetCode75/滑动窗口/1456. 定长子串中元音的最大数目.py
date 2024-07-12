class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def check(ch):
            return ch in ["a","e","i","o","u"]
        _max = 0
        n = len(s)
        for i in range(k):
            if check(s[i]):
                _max += 1
        cnt = _max
        for r in range(k,n):
            if check(s[r-k]):
                cnt -= 1
            if check(s[r]):
                cnt += 1
            _max = max(_max,cnt)
        return _max

s = Solution()
print(s.maxVowels(s = "abciiidef", k = 3))
print(s.maxVowels(s = "aeiou", k = 2))
print(s.maxVowels(s = "leetcode", k = 3))
print(s.maxVowels(s = "rhythms", k = 4))
print(s.maxVowels(s = "tryhard", k = 4))