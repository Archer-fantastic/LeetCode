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
    # 17. 电话号码的字母组合
    def letterCombinations(self, digits: str) -> List[str]:
        arr = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'],
               ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
               ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        def dfs(path,res,depth,size):
            if depth == size:
                res.append(path[:])
                if res == "": return []
                return res
            n = int(digits[depth])
            visit = [False for _ in range(len(arr[n]))]
            for i in range(len(arr[n])):
                if not visit[i]:
                    visit[i] = True
                    path+=arr[int(digits[depth])][i]

                    dfs(path,res,depth+1,size)

                    visit[i] = False
                    path=path[:-1]
            return res
        res = dfs(path="",res=[],depth=0,size=len(digits))
        return res

    # 39. 组合总和
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        def dfs(path,res,depth,_sum,size):
            if target == _sum:
                if path[:] not in res:
                    res.append(path[:])
                return
            if depth == size or target < _sum:
                return []
            n = len(candidates)
            visit = [False for _ in range(n)]
            for i in range(n):
                if not visit[i]:
                    visit[i] = True
                    if len(path)==0 or candidates[i] >= path[-1]:
                        path.append(candidates[i])
                        _sum += candidates[i]

                    dfs(path,res,depth+1,_sum,size)

                    if len(path) == 0 or candidates[i] >= path[-1]:
                        path.pop()
                        _sum -= candidates[i]
                    # visit[i] = False
            return res
        res = dfs(path=[], res=[], depth=0, _sum=0,size=target//candidates[0])
        return res

    # 22. 括号生成
    def generateParenthesis(self, n: int) -> List[str]:
        chars = ["(",")"]
        def judge(ss):
            score = 0
            for s in ss:
                if s == "(":
                    score+=1
                else:
                    score-=1
                if score < 0:
                    return -1
            return score

        def dfs(path,res,depth,size):
            if depth == size:
                if judge(path) == 0:
                    res.append(path[:])
                return
            visit = [False,False]

            for i in range(2):
                if not visit[i]:
                    visit[i] = True
                    path+=chars[i]
                    if judge(path) >= 0:
                        dfs(path,res,depth+1,size)
                    path=path[:-1]
            return res
        res = dfs(path="",res=[],depth=0,size=2*n)
        return res

    # 79. 单词搜索
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        t = len(word)
        def judge(s):
            return word.startswith(s)
        def dfs(visit,i,j,path,depth):
            if depth == t:
                return True
            target = False
            for k in range(4):
                if not visit[i][j]:
                    visit[i][j] = True
                    path+=board[i][j]
                    # if path == word: return True
                    if k==0 and j+1<n:
                        if judge(path):
                            target = dfs(visit,i,j+1,path,depth+1)
                    elif k==1 and i+1<m:
                        if judge(path):
                            target = dfs(visit,i+1,j,path,depth+1)
                    elif k==2 and i-1>=0:
                        if judge(path):
                            target = dfs(visit,i-1,j,path,depth+1)
                    elif k==3 and j-1>=0:
                        if judge(path):
                            target = dfs(visit,i,j-1,path,depth+1)
                    if target: return True
                    path=path[:-1]
                    visit[i][j] = False
            return target

        cnt = {}
        for i in range(26):
            cnt[chr(ord("A")+i)] = 0
            cnt[chr(ord("a")+i)] = 0
        for i in range(m):
            for j in range(n):
                cnt[board[i][j]] += 1
        for ss in word:
            cnt[ss] -= 1
        for c in cnt:
            if cnt[c] < 0 :
                return False

        visit = [[False for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = dfs(visit,i,j,"",0)
                if res: return res
        return False

    # 51. N 皇后
    def solveNQueens(self, n: int) -> List[List[str]]:
        m = n * 2 - 1
        ans = []
        col = [0] * n
        on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m

        def dfs(r: int) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
                return
            for c, on in enumerate(on_path):
                if not on and not diag1[r + c] and not diag2[r - c]:
                    col[r] = c
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场

        dfs(0)
        return ans



if __name__ == '__main__':
    nums = [1, 1, 3]
    solution = Solution()
    # res = solution.permute(nums)
    # print(res)
    # ==============================================================
    # print(solution.letterCombinations("23"))
    # print(solution.letterCombinations(""))
    # print(solution.letterCombinations("2"))
    # print(solution.letterCombinations("32323"))

    # ================================================================
    # print(solution.combinationSum(candidates = [2,3,6,7], target = 7))
    # print(solution.combinationSum(candidates = [2,3,5], target = 8))
    # print(solution.combinationSum(candidates = [2], target = 3))

    # ==================================================================
    # print(solution.generateParenthesis(1))
    # print(solution.generateParenthesis(2))
    # print(solution.generateParenthesis(3))
    # print(solution.generateParenthesis(4))
    # print(solution.generateParenthesis(5))
    # ==================================================================
    # print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    # print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
    # print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
    # print(solution.exist(board = [["B","A"]], word = "AB"))
    # print(solution.exist(board = [["B","A"]], word = "A"))
    # print(solution.exist(board = [["B","A"]], word = "B"))
    # print(solution.exist(board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], word = "aaaaaaaaaaaaa"))
    # ==================================================================

    print(solution.solveNQueens(4))
