class Solution(object):
    def minimumPerimeter(self, neededApples):
        a = 0
        while True:
            aa = a // 2
            # aa * (aa+1) * (aa+1) *4 - aa * (aa+1) * 2
            if aa * (aa + 1) * ((aa + 1) * 4 - 2) < neededApples:
                a += 2
            else:
                return 4 * a
        return -1
s = Solution()
print(s.minimumPerimeter(1))
print(s.minimumPerimeter(13))
print(s.minimumPerimeter(1000000000))