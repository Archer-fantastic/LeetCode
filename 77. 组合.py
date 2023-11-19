class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n,arr,k):
            if k <= 0 :
                return arr
            ans = []
            for idx in range(len(arr)):
                for i in range(arr[idx][-1]+1,n+1):

                    ans.append(arr[idx] + [i])
            return dfs(n,ans,k-1)
        return dfs(n,[[i] for i in range(1,n-k+2)],k-1)
