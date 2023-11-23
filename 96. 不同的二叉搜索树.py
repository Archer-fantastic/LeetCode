class Solution:
    def __init__(self):
        self.dic = {}

    def numTrees(self, n: int) -> int:
        # 字典已经记录过的值直接返回
        if n in self.dic:
            return self.dic[n]
        # 递归结束条件：n=0、n=1
        if n <= 1:
            self.dic[n] = 1
        else:
            ans = 0
            for i in range(n):
                ans += self.numTrees(i) * self.numTrees(n-i-1)
            self.dic[n] = ans
        return self.dic[n]

    def numTrees2(self, n: int) -> int:
        ans = [0]*(n+1)
        ans[0],ans[1] = 1,1
        for i in range(2,n+1):
            for j in range(1,i+1):
                ans[i] += ans[j-1] * ans[i-j]
        return ans[n]

s = Solution()
# print(s.numTrees(3))
for i in range(1,20):
    print(i,s.numTrees(i))