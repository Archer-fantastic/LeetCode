from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        def fun(n):
            if n == 1:
                return ["0","1"]
            elif n == 2:
                return ["01","10","11"]
            else:
                _list = fun(n-1)
                ans = []
                for item in _list:
                    if item[-1] == "0":
                        ans.append(item+"1")
                    else:
                        ans.append(item+"0")
                        ans.append(item+"1")
                return ans
        return fun(n)