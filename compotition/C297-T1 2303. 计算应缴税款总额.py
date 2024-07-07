class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        money = 0
        brackets.insert(0,[0,0])
        for idx in range(1,len(brackets)):
            money += (min(income,brackets[idx][0]) - brackets[idx-1][0]) * (brackets[idx][1] / 100.0)
            if income <= brackets[idx][0]:
                break
        return money