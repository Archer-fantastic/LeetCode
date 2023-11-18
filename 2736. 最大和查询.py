import bisect
from typing import List


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        dic = {}
        n = len(nums1)
        ans = []
        nums3 = [(nums1[i],nums2[i]) for i in range(n)]
        nums3 = sorted(nums3,key=lambda x:x[0])
        nums1 = sorted(nums1)
        for query in queries:
            if (query[0],query[1]) in dic:
                ans.append(dic[(query[0],query[1])])
                continue
            _max = -1
            idx = bisect.bisect_left(nums1,query[0])
            for i in range(idx,n):
                if nums3[i][1] >= query[1]:
                    _max = max(_max,nums3[i][0]+nums3[i][1])
            dic[(query[0],query[1])] = _max
            ans.append(_max)
        return ans

s = Solution()
print(s.maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]))
print(s.maximumSumQueries(nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]))
print(s.maximumSumQueries(nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]))