from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 以后就把dic换成defaultdict，时间和代码都会快一些
        dic = defaultdict(int)
        n = len(fruits)

        # 滑动窗口的变量，这里的judge条件换成了cnt
        left = 0
        cur_len = 0
        cur_max = 0
        cls_cnt = 0
        for i in range(n):
            cur_len += 1
            if dic[fruits[i]] == 0:
                cls_cnt += 1
            dic[fruits[i]] += 1
            while cls_cnt > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    cls_cnt -= 1
                cur_len -= 1
                left += 1
            cur_max = max(cur_max,cur_len)
        return cur_max
s = Solution()
print(s.totalFruit([1,2,1]))
print(s.totalFruit([0,1,2,2]))
print(s.totalFruit([1,2,3,2,2]))
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))