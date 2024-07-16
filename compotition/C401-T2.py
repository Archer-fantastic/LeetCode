class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        pre = [i+1 for i in range(n)]
        for i in range(k-1):
            for j in range(1,n):
                pre[j] = (pre[j]+pre[j-1])%(10**9+7)
        return pre[-1]

s = Solution()
print(s.valueAfterKSeconds(4,5))
print(s.valueAfterKSeconds(5,3))