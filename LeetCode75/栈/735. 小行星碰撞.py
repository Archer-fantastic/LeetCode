from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk =[]
        idx = 0
        n = len(asteroids)
        while idx < n:
            if len(stk) >0 and stk[-1] * asteroids[idx] < 0 and stk[-1]>0:
                if abs(stk[-1]) == abs(asteroids[idx]):
                    stk.pop()
                elif abs(stk[-1]) < abs(asteroids[idx]):
                    stk.pop()
                    continue
            else:
                stk.append(asteroids[idx])
            idx += 1
        return stk
s = Solution()
print(s.asteroidCollision(asteroids = [5,10,-5]))
print(s.asteroidCollision(asteroids = [5,-5]))
print(s.asteroidCollision(asteroids = [10,2,-5]))
print(s.asteroidCollision(asteroids = [-2,-1,1,2]))