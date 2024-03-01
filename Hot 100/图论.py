from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.g = grid
        self.m, self.n = len(self.g), len(self.g[0])

        def dfs(i, j):
            self.g[i][j] = "0"
            if i + 1 < self.m and self.g[i + 1][j] == "1": dfs(i + 1, j)
            if i - 1 >= 0 and self.g[i - 1][j] == "1": dfs(i - 1, j)
            if j + 1 < self.n and self.g[i][j + 1] == "1": dfs(i, j + 1)
            if j - 1 >= 0 and self.g[i][j - 1] == "1": dfs(i, j - 1)

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.g[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

    # 463. 岛屿的周长

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sum += 1 if i + 1 < m and grid[i + 1][j] == 0 else 0
                    sum += 1 if i - 1 >= 0 and grid[i - 1][j] == 0 else 0
                    sum += 1 if j + 1 < n and grid[i][j + 1] == 0 else 0
                    sum += 1 if j - 1 >= 0 and grid[i][j - 1] == 0 else 0
        return sum

    # 695. 岛屿的最大面积
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        self.g = grid
        self.m, self.n = len(self.g), len(self.g[0])

        def dfs(i, j):
            area = 0
            if 0 <= i < self.m and 0 <= j < self.n and self.g[i][j] == 1:
                area += 1
                self.g[i][j] = 0
                area += dfs(i + 1, j)
                area += dfs(i - 1, j)
                area += dfs(i, j + 1)
                area += dfs(i, j - 1)
            return area

        _max = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.g[i][j] == 1:
                    _max = max(_max, dfs(i, j))
        return _max

    # 207. 课程表
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 检查入度
        in_list = [0 for _ in range(numCourses)]
        # 记录邻接顶点
        dic = {i: [] for i in range(numCourses)}
        # 访问记录
        visit = [0 for _ in range(numCourses)]
        # 初始化邻接表和入度
        for l in prerequisites:
            dic[l[-1]].append(l[0])
            in_list[l[0]] += 1
        # print(in_list,dic)
        while sum(in_list) > 0:
            target = True
            for idx in range(numCourses):
                # 取出入度为0的顶点，将其邻接顶点的入度-1
                if in_list[idx] == 0 and visit[idx] == 0:
                    target = False
                    visit[idx] = 1
                    for i in dic[idx]:
                        in_list[i] -= 1
            # 若此时无入度为0的节点，则无法进行拓补排序
            if target: return False
        return True

    # 994. 腐烂的橘子
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        d = 0

        def get_tmp():
            return [[0 for _ in range(self.n)] for _ in range(self.m)]

        def judge():
            for i in range(self.m):
                for j in range(self.n):
                    if grid[i][j] == 1: return True
            return False

        while judge():
            tmp = get_tmp()
            for i in range(self.m):
                for j in range(self.n):
                    if grid[i][j] == 2:
                        if i - 1 >= 0 and grid[i - 1][j] == 1:
                            tmp[i - 1][j] = 2
                        if i + 1 < self.m and grid[i + 1][j] == 1:
                            tmp[i + 1][j] = 2
                        if j + 1 < self.n and grid[i][j + 1] == 1:
                            tmp[i][j + 1] = 2
                        if j - 1 >= 0 and grid[i][j - 1] == 1:
                            tmp[i][j - 1] = 2
            target = True
            for i in range(self.m):
                for j in range(self.n):
                    if tmp[i][j] == 2 and grid[i][j] == 1:
                        target = False
                        grid[i][j] = 2
            if target:
                return -1
            d += 1
        return d


s = Solution()
# s.numIslands(
#     grid=[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
# s.numIslands(
#     grid=[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
# print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
# print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))
# print(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
# print(s.canFinish(numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))

print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting(grid=[[0, 2]]))

class Trie:

    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        return self.words.count(word) >= 1


    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

obj = Trie1()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("apple"))
print(obj.search("apple"))
