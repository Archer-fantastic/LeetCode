class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        _len = len(height)
        l,r = 0,_len-1
        _max = 0
        while l <= r:
            _max = max(_max,min(height[l],height[r])*(r-l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return _max