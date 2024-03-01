from typing import List

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    # 回溯法：
    # 有且只有一个path存当前路径，一个标记数组visit存访问标记，res存最后的结果，size存数组长度，还有一个深度

        def dfs(visit,path,res,depth,size):
            if depth == size:
                res.append(path[:])
                return
            dic = set()
            for i in range(size):
                if not visit[i]:
                    if nums[i] in dic: continue
                    visit[i] = True
                    path.append(nums[i])
                    dic.add(nums[i])

                    dfs(visit,path,res,depth+1,size)

                    visit[i] = False
                    path.pop()
            return res
        n = len(nums)
        visit = [False for _ in range(n)]
        res = dfs(visit,path=[],res=[],depth=0,size=n)
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, state, res):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                if ((state >> i) & 1) == 0:
                    dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)

        size = len(nums)
        if size == 0:
            return []

        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)
        return res



    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def dfs(nums, size, depth, path, used, res):
    #         if depth == size:
    #             res.append(path[:])
    #             return
    #
    #         for i in range(size):
    #             if not used[i]:
    #                 used[i] = True
    #                 path.append(nums[i])
    #
    #                 dfs(nums, size, depth + 1, path, used, res)
    #
    #                 used[i] = False
    #                 path.pop()
    #         return res
    #     size = len(nums)
    #     if len(nums) == 0:
    #         return []
    #
    #     used = [False for _ in range(size)]
    #     res = []
    #     dfs(nums, size, 0, [], used, res)
    #     return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # 回溯法：
    # 有且只有一个path存当前路径，一个标记数组visit存访问标记，res存最后的结果，size存数组长度，还有一个深度

        def dfs(visit,path,res,depth,size):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not visit[i]:
                    visit[i] = True
                    path.append(nums[i])

                    dfs(visit,path,res,depth+1,size)

                    visit[i] = False
                    path.pop()
            return res
        n = len(nums)
        visit = [False for _ in range(n)]
        res = dfs(visit,path=[],res=[],depth=0,size=n)
        return list(set(res))

if __name__ == '__main__':
    nums = [1, 1, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)

