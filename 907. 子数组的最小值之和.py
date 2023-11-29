from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pre= [0xFFFF]
        for num in arr:
            pre.append(min(num,pre[-1]))
        print(pre)
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if pre[j+1] != pre[i+1]:
                    ans += pre[j+1]
                else:
                    ans += min(arr[i:j+1])
                ans %= 10**9+7
        return ans + sum(arr)
s = Solution()
print(s.sumSubarrayMins([3,1,2,4]))
print(s.sumSubarrayMins([11,81,94,43,3]))