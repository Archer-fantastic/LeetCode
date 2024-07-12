from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 1
        flag = 1
        i = 1
        cnt = 1
        for idx in range(1,len(chars)):
            if chars[idx]==chars[idx-1]:
                if flag == 1:
                    # ans += 1
                    flag = 0
                cnt += 1
            if chars[idx]!=chars[idx-1]:
                if cnt>1:
                    for cc in str(cnt):
                        chars[i] = cc
                        i += 1
                        ans += 1
                chars[i] = chars[idx]
                i+=1
                ans += 1
                cnt = 1
                flag = 1
        if cnt > 1:
            for cc in str(cnt):
                chars[i] = cc
                i += 1
                ans +=1
        print(chars)
        return ans
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(s.compress(["a","a","a","b","b","b","c","c","c","d","e","e","e","e","e","e","e","e","e","e","e","e"]))