from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                ans += 1 if (hours[i]+hours[j])%24 == 0 else 0
        return ans