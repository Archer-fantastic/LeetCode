from typing import List
class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars =sorted(hBars)
        vBars = sorted(vBars)
        _h = 1
        _v = 1
        _max_h = 0
        _max_v = 0
        hBars.append(n+2)
        vBars.append(m+2)
        idx = 2
        for h in hBars:
            if idx == n+2:
                _max_h = max(_max_h, idx - _h)
                break
            if idx == h:
                idx+=1
                continue
            while h != idx:
                _max_h = max(_max_h, idx - _h)
                _h = h
                idx += 1
        idx = 2
        for v in vBars:
            if idx == m+2:
                _max_v = max(_max_v, idx - _v)
                break
            if idx == v:
                idx+=1
                continue
            while v != idx:
                _max_v = max(_max_v, idx - _v)
                _v = v
                idx += 1
        print(_max_h,_max_v)
        return min(_max_h,_max_v) * min(_max_h,_max_v)
s = Solution()
# print(s.maximizeSquareHoleArea(n = 2, m = 4, hBars = [3,2], vBars = [4,2]))
print(s.maximizeSquareHoleArea(n = 14, m = 4, hBars = [13], vBars = [4,3,2,5]))
