class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while len(s[left:i+1]) != len(set(s[left:i+1])):
                cur_len -= 1
                left += 1
            max_len = max(max_len,cur_len)
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        max_len = 0
        cur_len = 0
        arr = []
        for i in range(n):
            cur_len += 1
            arr.append(s[i])
            while len(arr) != len(set(arr)):
                arr.pop(0)
                cur_len -= 1
                left += 1
            max_len = max(max_len, cur_len)
        return max_len
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))