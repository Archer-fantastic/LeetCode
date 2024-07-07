class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        word = list(word)
        if word[-1] == 'z':
            word += 'b'
        elif word[-1] == 'y':
            word += 'a'
        else:
            word += chr(ord(word[-1])+2)
        ans = 0
        for i in range(n-1):
            if abs(ord(word[i+1]) - ord(word[i])) <= 1:
                word[i+1] = chr(max(ord(word[i]),ord(word[i+2])+2))
                ans += 1
        return ans
s = Solution()
print(s.removeAlmostEqualCharacters("aaaaa"))
print(s.removeAlmostEqualCharacters("abddez"))
print(s.removeAlmostEqualCharacters("zyxyxyz"))
