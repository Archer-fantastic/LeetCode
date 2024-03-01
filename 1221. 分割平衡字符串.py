class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = {"L":1,"R":-1}
        tmp = 0
        ans = 0
        for a in s:
            tmp+=dic[a]
            if tmp == 0:
                ans += 1
        return ans