from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.d = []
        self.dic = {kingName:[]}

    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)
        self.dic[childName] = []

    def death(self, name: str) -> None:
        self.d.append(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(root):
            if root:
                if root not in self.d:
                    res.append(root)
                for child in self.dic[root]:
                    dfs(child)
        dfs("king")
        return res




# Your ThroneInheritance object will be instantiated and called as such:
obj = ThroneInheritance("king")
obj.birth("king","A")
obj.birth("king","B")
obj.birth("king","C")
obj.birth("king","D")
obj.birth("A","E")
obj.birth("C","F")
obj.birth("E","G")
print(obj.getInheritanceOrder())
obj.death("A")
print(obj.getInheritanceOrder())