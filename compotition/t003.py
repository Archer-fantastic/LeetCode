from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # 三叉树
        def f1(arr):return arr[0] + arr[1]
        def f2(arr):return arr[0] + arr[-1]
        def f3(arr):return arr[-1] + arr[-2]
        def f(q1,num):
            cur_max = 1
            while True:
                new_q1 = []
                target = True
                for n in q1:
                    if len(n[-1]) < 2 or (f1(n[-1]) != num and f2(n[-1]) != num and f3(n[-1]) != num):
                        continue
                    if len(n[-1])>=2 and f1(n[-1]) == num:
                        new_q1.append([n[0]+1,n[-1][2:]])
                        target = False
                    if len(n[-1])>=2 and f2(n[-1]) == num:
                        new_q1.append([n[0]+1,n[-1][1:-1]])
                        target = False
                    if len(n[-1])>=2 and f3(n[-1]) == num:
                        new_q1.append([n[0]+1,n[-1][:-2]])
                        target = False
                if target:
                    return max([t[0] for t in q1])
                q1 = new_q1
        return max(f([[1,nums[2:]]],f1(nums)),f([[1,nums[1:-1]]],f2(nums)),f([[1,nums[:-2]]],f3(nums)))
s = Solution()
print(s.maxOperations([3,2,1,2,3,4]))
print(s.maxOperations([3,2,6,1,4]))
print(s.maxOperations([1,1,2,3,2,2,1,3,3]))










