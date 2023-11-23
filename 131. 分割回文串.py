import time
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        t1 = time.time()
        # get_comb给定字符串s，返回字符串中回文串的位置
        #
        def get_comb(s):
            ans = []
            n = len(s)
            for i in range(n):
                for j in range(i+2,n+1):
                    if judge(s[i:j]):
                        ans.append((i,j-1))
            return ans

        def judge(s):
            return s == s[::-1]

        def dfs(dic,comb):
            target = 0
            ans = []
            for c in comb:
                if not dic[c[-1]]:
                    ans.append(c)
                    continue
                target = 1
                for cc in dic[c[-1]]:
                    ans.append(c + [cc])
            if target == 0:
                return ans
            return dfs(dic,ans)


        # print(combs)
        # print(dic)
        def get_areas(combs):
            ans = []
            for c in [[comb] for comb in combs]:
                _tmp = dfs(dic,[c])
                ans += _tmp
                # print(ans)
                for t in _tmp:
                    _len = len(t) - 1
                    for i in range(2 ** _len-1):
                        code = "1" + str(bin(i))[2:].zfill(_len)
                        _comb = []
                        for idx,_code in enumerate(code):
                            if _code == "1":
                                _comb.append(t[idx])
                        if _comb not in ans:
                            ans.append(_comb)
                # print(ans)
                # print("--"*100)
            return ans
        def get_ans(ans):
            res = [[ss for ss in s]]
            for a in ans:
                idx = 0
                idx2 = 0
                _res = []
                while idx < len(s):
                    if idx2 < len(a):
                        cur_area = a[idx2]
                    if idx2 < len(a) and cur_area[0] == idx:
                        _res.append(s[cur_area[0]:cur_area[1]+1])
                        idx = cur_area[1]+1
                        idx2 += 1
                    else:
                        _res.append(s[idx])
                        idx += 1
                # print(a,"-->",_res)
                if _res not in res:
                    res.append(_res)
            return res
        # 递归处理全部字符都一致的情况
        if len(s) == 1:
            return [[s]]
        if len(set(list(s))) == 1:
            ans = []
            tmp = self.partition(s[1:])
            for t in tmp:
                ans.append(t + [s[0]])
                t[-1] += s[0]
                ans.append(t)
            return ans
        print("原始字符串:",s)


        combs = get_comb(s)
        print("回文子串的位置:",combs)
        n = len(combs)
        dic = {}
        for idx1 in range(n):
            dic[combs[idx1]] = []
            for idx2 in range(idx1+1,n):
                if combs[idx2][0] > combs[idx1][1]:
                    dic[combs[idx1]].append(combs[idx2])
        print("构造一个用来枚举的字典：",dic)
        t2 = time.time()
        ans = get_areas(combs)

        print("可以得到一个用数字表示的答案：",ans)
        t3 = time.time()
        res = get_ans(ans)
        print("最后把答案翻译成字符串格式",res)
        t4 = time.time()
        # print(t2-t1)
        # print(t3-t2)
        # print(t4-t3)
        # return len(res)
        return res



s = Solution()
print(s.partition("abcdedcba"))
print(s.partition("ebabacababf"))
# print(s.partition("aab"))
# print(s.partition("a"))
# print(s.partition("a"*7 + "b" + "a"*7))
for i in range(2,10):
    print(" ",len(s.partition("a"*i)),"\t",s.partition("a"*i))
# print(s.partition("abababababababab"))
# print(s.partition("ab"))

