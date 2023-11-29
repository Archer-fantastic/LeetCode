class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i+1 for i in range(1001)]

    def popSmallest(self) -> int:
        return self.arr.pop(0)


    def addBack(self, num: int) -> None:
        if num not in self.arr:
            idx = 0
            while self.arr[idx] < num:
                idx += 1
            self.arr.insert(idx,num)

def fun(commands,parms):
    obj = SmallestInfiniteSet()
    n = len(commands)
    for i in range(1,n):
        print(f"round {i}",end=" ")
        if commands[i] == "addBack":
            obj.addBack(parms[i][0])
        if commands[i] == "popSmallest":
            obj.popSmallest()
        print(obj.arr[:20])
fun(
["SmallestInfiniteSet","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","popSmallest"],
    [[],[],[1],[],[],[],[2],[3],[],[]]
)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)