class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        nums = []
        for idx,d in enumerate(number):
            if d == digit:
                nums.append(int(number[:idx] + number[idx+1:]))
        # print(nums)
        return str(max(nums))