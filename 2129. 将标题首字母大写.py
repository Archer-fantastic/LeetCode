class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split(" ")
        for idx,word in enumerate(l):
            if len(word)<=2:
                l[idx] = word.lower()
            l[idx] = word.title()
        return "".join(l)
