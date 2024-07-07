from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        left = [0,nums[0]]
        right = [nums[-1]]
        _min = nums[0]
        for idx in range(2,len(nums)-1):
            _min = min(_min,nums[idx-1])
            left.append(_min)
        _min = nums[-1]
        for idx in range(len(nums)-3,0,-1):
            _min = min(_min,nums[idx+1])
            right.append(_min)
        right.append(0)
        right = right[::-1]
        _min = 0xFFFFFFFF

        print("left:\t",left)
        print("right:\t",right)
        print("nums:\t",nums)

        for i in range(1,len(nums)-1):
            if nums[i] > left[i] and nums[i] > right[i]:
                _min = min(_min,nums[i]+left[i]+right[i])
        return -1 if _min==0xFFFFFFFF else _min

s = Solution()
print(s.minimumSum([8,6,1,5,3]))
print(s.minimumSum([5,4,8,7,10,2]))
print(s.minimumSum([6,5,4,3,4,5]))