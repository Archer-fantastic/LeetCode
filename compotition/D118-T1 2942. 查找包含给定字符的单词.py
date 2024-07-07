from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for idx,word in enumerate(words):
            if word.count(x) > 0:
                ans.append(idx)
        return ans