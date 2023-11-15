import copy


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        arr = [[],[],['a','b','c'],['d','e','f'],
               ['g','h','i'],['j','k','l'],['m','n','o'],
               ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        if len(digits) > 0:
            ans = arr[int(digits[0])]
        else:
            return []
        for d in digits[1:]:
            _ans = copy.deepcopy(ans)
            ans = []
            for a in _ans:
                for b in arr[int(d)]:
                    ans.append(a+b)
        return ans