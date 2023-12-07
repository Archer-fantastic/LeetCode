import math


class Solution:
    def minWindow(self, s, t):
        # 初始化两个观察字典
        # lookup1是用来比较的模版字典，lookup2要记录当前的窗口中的所求字母数量
        lookup1 = {tt: 0 for tt in t}
        lookup2 = {tt: 0 for tt in t}
        for tt in t:
            lookup1[tt] += 1

        # 用来判断当前窗口是否合法的函数
        def judge(lookup1, lookup2):
            for k in lookup1:
                if lookup1[k] < lookup2[k]:
                    return False
            return True
        # left和i分别指的是慢指针和快指针
        n = len(s)
        left = 0
        min_len = math.inf
        cur_len = 0
        sub_str = ""

        for i in range(n):
            # 向右扩张窗口，操作cur_len，一切cur的东西，还有lookup
            if s[i] in lookup2:
                lookup2[s[i]] += 1
            cur_len += 1

            # 查看是否合法，合法就收缩窗口
            while judge(lookup2, lookup1):  #合法
                # 修改当前最小/最大值，记录答案
                if cur_len < min_len:
                    min_len = cur_len
                    sub_str = s[left:i + 1]
                # 收缩窗口，也要操作cur_len，一切cur的东西，还有lookup
                if s[left] in lookup2:      #最左侧字母出去
                    lookup2[s[left]] -= 1
                left += 1
                cur_len -= 1

        return sub_str
