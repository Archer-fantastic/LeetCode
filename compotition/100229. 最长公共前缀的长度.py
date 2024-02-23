import random
import time
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def fun(a,b):
            lcp = 0
            for tmp in zip(str(a),str(b)):
                if len(set(tmp)) == 1:
                    lcp += 1
                else:
                    break
            return lcp

            # _min = min(a,b)
            # _max = a + b - _min
            # _max = _max // (10 ** (len(str(_max)) - len(str(_min))))
            # while _max != _min:
            #     _max //= 10
            #     _min //= 10
            # if _max == 0:
            #     return 0
            #
            # return len(str(_max))
        arr1 = sorted(list(set(arr1)),reverse=True)
        arr2 = sorted(list(set(arr2)),reverse=True)
        l1 = len(arr1)
        l2 = len(arr2)
        _max = 0
        for i in range(l1):
            if len(str(arr1[i])) <= _max:
                break
            t3 = time.time()
            for j in range(l2):
                if len(str(arr2[j])) <= _max:
                    continue
                _max = max(_max,fun(arr1[i],arr2[j]))
            t4 = time.time()
            print(t4-t3,_max , len(str(arr1[i])))

        return _max
s= Solution()
# print(s.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]))
# print(s.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]))
print(s.longestCommonPrefix(arr1 = [random.randint(1,10**7) for i in range(5 * 10**4)], arr2 = [random.randint(1,10**7) for j in range(5 * 10**4)]))
# print(s.longestCommonPrefix([474,2907,2219,1527,1993,1847,4205,2666,3835,583,1336,1338,2432,2406,710,3927,4138,3492,2823,2857,3051,81,4356,1752,2565,1593,247,3067,4039,309,4400,2058,3671,2989,4111,4301,862,2845,1369,1208,4940,1780,2152,419,133,835,4841,773,3148,1301],
# [2918,3956,2242,2824,1235,562,1844,4315,1477,4471,2893,933,4957,649,3534,2169,4716,1534,497,4744,464,3,2608,549,66,2169,4183,1900,2962,1985,3895,2431,3694,985,2901,4929,3851,3551,3485,4701,3922,4849,659,3387,1428,1101,4264,2518,3982,2826]))
