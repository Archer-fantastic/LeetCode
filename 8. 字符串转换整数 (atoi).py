class Solution(object):
    def myAtoi(self, s):
        target = 1
        ans = "0"
        s = s.strip()
        if s == "":
            return 0
        if s[0] == "-":
            target = -1
            s = s[1:]
        elif s[0] == "+":
            target = 1
            s = s[1:]
        for ss in s:
            if ord("0")<= ord(ss) <= ord("9"):
                ans += ss
                ans_target = 1
            else:
                break
        return min(max(target * int(ans),-pow(2,31)),pow(2,31) - 1)