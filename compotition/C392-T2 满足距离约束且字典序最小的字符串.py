class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        dic1 = {chr(ord('a')+i):i+1 for i in range(26)}
        res = ""
        for idx,ss in enumerate(s):
            d = min(27 - dic1[ss],dic1[ss]-1)
            if k >= d:
                k-=d
                res += "a"
            else:
                res += chr(ord(ss)-k)
                break
        res += s[idx+1:]
        return res

s = Solution()
print(s.getSmallestString(s = "zbbz", k = 3))
print(s.getSmallestString(s = "xaxcd", k = 4))
print(s.getSmallestString(s = "lol", k = 0))
print(s.getSmallestString(s = "a", k = 0))
