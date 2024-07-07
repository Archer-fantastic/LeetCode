class Solution:

    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        my_str = ["0" for i in range(n)]
        for idx,ss in enumerate(s):
            if ss in ["a", "e", "i", "o", "u"]:
                my_str[idx] = "1"
        if my_str.count("1") == 0:
            return 0
        ans = 0

        for i in range(n):
            count1 = 0
            count2 = 0
            for j in range(i+1,n+1):
                if my_str[j-1] == "0":
                    count1 += 1
                else:
                    count2 += 1
                _len = j-i
                if count1!=count2 or _len % 2 == 1 or _len//2 * _len//2 % k != 0:
                    continue
                # if count1 == count2:
                ans += 1

        return ans
# print("ab"*500)
s = Solution()
print(s.beautifulSubstrings(s = "baeyh", k = 2))
print(s.beautifulSubstrings(s = "abba", k = 1))
print(s.beautifulSubstrings(s = "bcdf", k = 1))
print(s.beautifulSubstrings(s = "ab"*1000, k = 2))