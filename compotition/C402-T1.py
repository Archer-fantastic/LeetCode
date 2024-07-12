from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        dic = {hour%24:0 for hour in hours}
        for hour in hours:
            dic[hour%24] += 1
        print(dic)
        ans = 0
        if 12 in dic:
            ans += int((dic[12]*(dic[12]-1)) / 2)
        if 0 in dic:
            ans += int((dic[0]*(dic[0]-1)) / 2)

        for hour in hours:
            if hour%24 == 12 or hour%24 == 0:
                continue
            elif 24-(hour%24) in dic and dic[24-(hour%24)]>0:
                ans += (dic[24-(hour%24)] * dic[hour%24])
                dic[24 - (hour % 24)] = -1
                dic[hour % 24] = -1
        return ans

s = Solution()
print(s.countCompleteDayPairs([12,12,30,24,24]))
print(s.countCompleteDayPairs([13,11]))
print(s.countCompleteDayPairs([72,48,24,3]))
print(s.countCompleteDayPairs([12,18,29,19,27,5]
))