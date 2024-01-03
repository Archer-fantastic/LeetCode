from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n1 = len(player1)
        n2 = len(player2)
        for idx in range(n1-1,-1,-1):
            if (idx-1 >= 0 and player1[idx-1] == 10) or (idx-2 >= 0 and player1[idx-2] == 10):
                player1[idx] *= 2
        for idx in range(n2-1,-1,-1):
            if (idx-1 >= 0 and player2[idx-1] == 10) or (idx-2 >= 0 and player2[idx-2] == 10):
                player2[idx] *= 2
        sum1 = sum(player1)
        sum2 = sum(player2)
        if sum1 == sum2:
            return 0
        elif sum1 > sum2:
            return 1
        else:
            return 2
s = Solution()
print(s.isWinner(player1 = [4,10,7,9], player2 = [6,5,2,3]))
print(s.isWinner(player1 = [3,5,7,6], player2 = [8,10,10,2]))
print(s.isWinner(player1 = [2,3], player2 = [4,1]))
print(s.isWinner(player1 = [10,2,2,3], player2 = [3,8,4,5]))