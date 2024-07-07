class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple = sorted(apple,reverse=True)
        s =sum(apple)
        capacity = sorted(capacity,reverse=True)
        ans = 0
        for c in capacity:
            if s > 0:
                ans += 1
                s -= c
        return ans