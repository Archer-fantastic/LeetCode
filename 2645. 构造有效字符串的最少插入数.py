class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        idx = 0
        ans = 0
        while idx < n:
            if word[idx] == "c":
                ans += 2
                idx += 1
            elif idx + 1 < n and word[idx] == "b" and word[idx+1] == "c":
                ans += 1
                idx += 2
            elif word[idx] == "b":
                ans += 2
                idx += 1
            elif idx + 2 < n and word[idx] == "a" and word[idx+1] == "b" and word[idx+2]=="c":
                idx += 3
            elif idx + 1 < n and word[idx] == "a" and word[idx+1] == "b":
                ans += 1
                idx += 2
            elif idx + 1 < n and word[idx] == "a" and word[idx+1] == "c":
                ans += 1
                idx += 2
            else:
                ans += 2
                idx += 1
        return ans
    def addMinimum2(self, word: str) -> int:
        n = len(word)
        idx = 0
        ans = 0
        while idx < n:
            if word[idx] == "c":
                ans += 2
                idx += 1
            elif idx + 1 < n and word[idx] == "b" and word[idx+1] == "c":
                ans += 1
                idx += 2
            elif word[idx] == "b":
                ans += 2
                idx += 1
            elif idx + 2 < n and word[idx] == "a" and word[idx+1] == "b" and word[idx+2]=="c":
                idx += 3
            elif idx + 1 < n and word[idx] == "a" and (word[idx+1] == "b" or word[idx+1] == "c"):
                ans += 1
                idx += 2
            else:
                ans += 2
                idx += 1
        return ans

s = Solution()
print(s.addMinimum(word = "b"))
print(s.addMinimum(word = "aaa"))
print(s.addMinimum(word = "abc"))