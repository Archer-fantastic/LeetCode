from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic = {i: [] for i in range(1, 4)}
        for time in times:
            dic[time[0]].append((time[1], time[2]))
        print(dic)
        target = [0 for _ in range(n + 1)]

        def dfs(i):
            if target[i] == 1:
                return 0
            cost = 0
            target[i] = 1
            # print(i)
            _max = 0
            if i in dic:
                for j in dic[i]:
                    if target[j[0]] == 1:
                        continue
                    cost += j[1]
                    _cost = dfs(j[0])
                    cost += _cost
                    _max = min(_max,cost)
                    cost -= _cost
                    cost -= j[1]
            return _max
        cost = dfs(k)
        return -1 if sum(target) < n else cost


s = Solution()
print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
print(s.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))
print(s.networkDelayTime(times=[[1, 2, 1],[1, 3, 3],[1, 4, 1],[2, 5, 2],[2, 6, 2],[2, 7, 2],[3, 8, 1],[3, 9, 2],[3, 10, 3]], n=10, k=1))
