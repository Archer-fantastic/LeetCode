from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _list = {i:0 for i in arr}
        for num in arr:
            _list[num] += 1
        print(len(set(_list.values())) , len(set(arr)))
        return len(set(_list.values())) == len(set(arr))
s = Solution()
s.uniqueOccurrences([1,2,2,1,1,3])