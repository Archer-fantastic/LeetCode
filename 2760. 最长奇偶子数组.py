class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n, ans, i = len(nums), 0, 0
        while i < n:
            if nums[i] % 2 != 0 or nums[i] > threshold:
                i += 1
                continue
            j, cur = i + 1, nums[i] % 2
            while j < n:
                if nums[j] > threshold or nums[j] % 2 == cur: break
                cur, j = nums[j] % 2, j + 1
            ans = max(ans, j - i)
            i = j
        return ans