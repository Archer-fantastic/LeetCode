from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        nums = list(zip(dic.keys(), dic.values()))
        nums.sort(key=lambda x: (-x[1],x[0]))
        return [nums[i][0] for i in range(k)]


s = Solution()
print(s.topKFrequent( words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2))
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
print(s.topKFrequent(["i","love","leetcode","i","love","coding"], k = 3))
