import collections


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            ch = s[left] if ord(s[left]) <= ord(s[right]) else s[right]
            s[left],s[right] = ch,ch
            left += 1
            right -= 1
        return "".join(s)

s = Solution()
print(s.makeSmallestPalindrome("egcfe"))
print(s.makeSmallestPalindrome("abcd"))
print(s.makeSmallestPalindrome("seven"))
print(s.makeSmallestPalindrome("abcdefga"))
print(s.makeSmallestPalindrome("aa"))