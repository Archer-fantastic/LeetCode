class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank >= 5:
            mainTank -= 5
            res += 50
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1

        return res + 10*mainTank
s = Solution()
print(s.distanceTraveled(1,2))
