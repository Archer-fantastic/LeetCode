from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n,arr,k):
            if k <= 0 :
                return arr
            ans = []
            for idx in range(len(arr)):
                for i in range(arr[idx][-1]+1,n+1):
                    ans.append(arr[idx] + [i])
            return dfs(n,ans,k-1)
        return dfs(n,[[i] for i in range(1,n-k+2)],k-1)
    def restoreIpAddresses(self, s: str) -> List[str]:
        def add(s,arr):
            ss = ""
            idx = 0
            for num in arr:
                ss += (s[idx:num] + ".")
                idx = num
            return ss + s[idx:]
        def judge(s):
            ss = s.split(".")
            for sss in ss:
                if int(sss) > 255 or (sss[0] == "0" and len(sss) > 1):
                    return False
            return True
        n = len(s)
        if n == 4:
            return [f"{s[0]}.{s[1]}.{s[2]}.{s[3]}"]
        elif n < 4:
            return []
        elif n == 12:
            ss = f"{s[:3]}.{s[3:6]}.{s[6:9]}.{s[9:12]}"
            if judge(ss):
                return [ss]
            else:
                return []


        ans = []
        conbines = self.combine(n-1,3)
        for conbine in conbines:
            if conbine[1]-conbine[0] > 3 or conbine[2]-conbine[1] > 3 or n-conbine[2] > 3:
                continue
            ss = add(s,conbine)
            if judge(ss):
                ans.append(ss)
        return ans