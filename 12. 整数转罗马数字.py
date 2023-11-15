class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dic = {4:"IV",9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM",1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""
        while num > 0:
            idx = 0
            while num_list[idx]>num:
                idx += 1
            ans += roman_dic[num_list[idx]]
            num -= num_list[idx]
        return ans