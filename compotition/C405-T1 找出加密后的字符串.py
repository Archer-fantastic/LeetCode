class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k%len(s)
        s = s[k:] + s[:k]
        return s