from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        k = 1
        left1 = 0
        for right in range(1, len(hBars)):
            if hBars[right] == hBars[right - 1] + 1:
                k = max(k, right - left1 + 1)
            else:
                left1 = right
        c = 1
        left2 = 0
        for right in range(1, len(vBars)):
            if vBars[right] == vBars[right - 1] + 1:
                c = max(c, right - left2 + 1)
            else:
                left2 = right
        return min(c + 1, k + 1) ** 2