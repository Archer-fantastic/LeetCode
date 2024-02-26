from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(1,1+numRows):
            # [0,0]
            l = []
            for j in range(i+1):
                if j - 1 < 0:
                    l.append(arr[i-1][j])
                elif j >= i:
                    l.append(arr[i-1][j-1])
                else:
                    l.append(arr[i-1][j-1] + arr[i-1][j])
            arr.append(l)
        print(arr)
s = Solution()
s.generate(5)
s.generate(1)