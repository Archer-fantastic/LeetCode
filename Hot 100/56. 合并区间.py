from typing import List


class Solution:
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        t = [0 for i in range(10**4 + 1)]
        for interval in intervals:
            for j in range(interval[0],interval[1]+1):
                t[j] = 1
        ans = []
        start = -1
        end = -1
        for i in range(len(t)):
            if t[i] == 1 and start < 0:
                start = i
            if t[i] == 0 and start>0 and end < 0:
                ans.append([start,i-1])
                start = -1
        return ans

    def judge(self, a, b):
        if a[1] < b[0] or b[1] < a[0]:
            return False
        return True

    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        ans = [intervals[0]]
        for idx in range(1,len(intervals)):
            if idx <= len(intervals)-1 and self.judge(ans[-1], intervals[idx]):
                ans[-1][0] = min(intervals[idx][0], ans[-1][0])
                ans[-1][1] = max(intervals[idx][-1], ans[-1][-1])
            else:
                ans.append(intervals[idx])
        return ans
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([[1,4],[5,6]]))
print(s.merge([[1,4],[0,2],[3,5]]))
