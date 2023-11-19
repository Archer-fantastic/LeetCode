class Solution(object):
    def judge(self,a,b):
        if a[1] < b[0] or b[1] < a[0]:
            return False
        return True
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals,key=lambda x:x[0])
        print(intervals)
        idx = 0
        while idx < len(intervals)-1:
            if self.judge(intervals[idx],intervals[idx+1]):
                intervals[idx][-1] = max(intervals[idx][-1],intervals[idx+1][-1])
                intervals[idx][0] = min(intervals[idx][0],intervals[idx+1][0])
                intervals.pop(idx+1)
                idx -= 1
                idx = max(idx,0)
            else:
                idx += 1
        return intervals