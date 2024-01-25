class Solution:
    def minLength(self, s: str) -> int:
        while s.count("AB") + s.count("CD") > 0 :
            s = s.replace("AB","").replace("CD","")
        return len(s)
s = Solution()
print(s.minLength("ABFCACDB"))