class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # 1,0 1,2 3,2
        _max = max(red,blue)
        _min = red + blue - _max
        a,b=0,0
        high = 0
        while True:
            if _max>=max(a,b) and _min>=min(a,b):
                high+=1
            else:
                break
            if high % 2 == 1:
                a += high
            else:
                b += high
        return high - 1

s = Solution()
print(s.maxHeightOfTriangle(2,4))
print(s.maxHeightOfTriangle(2,1))
print(s.maxHeightOfTriangle(1,1))
print(s.maxHeightOfTriangle(10,1))
