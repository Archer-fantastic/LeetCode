class Solution:
    def stringCount(self, n: int) -> int:
        M = (26 ** n) % (10 ** 9 + 7)
        A = (25 ** n) % (10 ** 9 + 7)
        B = A
        C = A
        D = (n * (25 ** (n-1))) % (10 ** 9 + 7)
        AB = (24 ** n) % (10 ** 9 + 7)
        AC = AB
        BC = AB
        AD = (n * (24 ** (n-1))) % (10 ** 9 + 7)
        BD = AD
        ABC = (23 ** n) % (10 ** 9 + 7)
        ABD = (n * (23 ** (n-1))) % (10 ** 9 + 7)

        return (M-A-B-C-D+AB+AC+AD+BC+BD-ABC-ABD + (10 ** 9 + 7))% (10 ** 9 + 7)