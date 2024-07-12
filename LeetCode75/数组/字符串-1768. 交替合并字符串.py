class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2 = len(word1),len(word2)
        idx1,idx2=0,0
        ans = ""
        while idx1<l1 and idx2<l2:
            ans += word1[idx1]+word2[idx2]
            idx1+=1
            idx2+=1

        if idx1<l1 or idx2<l2:
            if idx1<l1:
                ans += word2[idx2:]
            else:
                ans += word1[idx1:]
        return ans
