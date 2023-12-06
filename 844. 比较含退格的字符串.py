class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for ss in s:
            if ss == "#" and len(stack) > 0:
                stack.pop()
            else:
                stack.append(ss)
        s1 = "".join(stack)
        stack = []
        for tt in t:
            if tt == "#" and len(stack) > 0:
                stack.pop()
            elif tt != "#":
                stack.append(tt)
        s2 = "".join(stack)
        print(s1,s2)
        return s1 == s2

# s = Solution()
# print(s.backspaceCompare("y#fo##f","y#f#o##f"))