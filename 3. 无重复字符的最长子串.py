class Solution(object):
    def getLen(self,s):
        return len(set(s))
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        _len = 0
        for idx,sub in enumerate(s):
            end = idx
            if self.getLen(s[start:end+1]) == end - start + 1:
                if end - start + 1 > _len:
                    _len = end - start + 1
            else:
                start = s.index(sub,start,end+1) + 1
        return _len
    # *****************

    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        n = len(s)
        dic = set()
        cur_len = 0
        idx = 0
        left = 0
        max_len = 0
        while idx < n:
            cur_len += 1
            while s[idx] in dic:
                dic.remove(s[left])
                left += 1
                cur_len -= 1
            dic.add(s[idx])
            max_len = max(max_len, cur_len)
            idx += 1
        return max_len