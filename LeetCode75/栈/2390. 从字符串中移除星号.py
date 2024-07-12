class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for ss in s:
            if ss == "*" and len(stk) != 0:
                stk.pop()
            else:
                stk.append(ss)
        return "".join(stk)