class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def judge(s1, s2):
            if s1 == s2:
                return s1
            if len(s1) == 0:
                return s2

            l1 = len(s1)
            l2 = len(s2)
            if l2 == 0:
                return s1
            if l1 > l2:
                return s2
            elif l1 < l2:
                return s1
            else:
                for i in range(l1):
                    if s1[i] == s2[i]:
                        continue
                    elif ord(s1[i]) > ord(s2[i]):
                        return s2
                    else:
                        return s1

        dic = {}
        for s in arr:
            res = []
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    res.append(s[i:j])
            for r in list(set(res)):
                if r in dic:
                    dic[r] += 1
                else:
                    dic[r] = 1
        # print("dic",dic)
        ans = []
        for s in arr:
            res = ""
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if dic[s[i:j]] == 1:
                        # print(i,j,res,s[i:j])
                        res = judge(res, s[i:j])
                        # print(res)

            ans.append(res)
        return ans
