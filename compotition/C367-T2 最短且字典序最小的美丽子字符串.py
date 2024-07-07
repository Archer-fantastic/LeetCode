class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l, r = 0, 0
        ans = ''
        curlen = 1
        minlen = len(s)
        curcount = 0
        for l in range(len(s)):
            curlen -= 1
            curcount = s[l:r + 1].count('1')
            while r < len(s) and curcount < k:
                r += 1
                curlen += 1
                curcount = \
                    s[l:r + 1].count('1')
            # print(ans,s[l:r+1])
            if curcount == k and minlen > curlen:
                minlen = curlen
                ans = s[l:r + 1]
            elif curcount == k and minlen == curlen and int(ans, 2) > int(s[l:r + 1], 2):
                minlen = curlen
                ans = s[l:r + 1]
            # print(ans,s[l:r+1])

        return ans

