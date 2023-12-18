from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        n = len(batteryPercentages)
        for idx,b in enumerate(batteryPercentages):
            if b > 0:
                for i in range(idx+1,n):
                    if batteryPercentages[i] > 0:
                        batteryPercentages[i] -= 1
                res += 1
        return res
s = Solution()
print(s.countTestedDevices([1,1,2,1,3]))