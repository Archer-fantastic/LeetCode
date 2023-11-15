class Solution(object):
    def reverse(self, x):
        x = str(x)
        if x[0] == '-':
            sym = "-"
            x = x[1:]
        else:
            sym = ""
        x = x[::-1]
        ans = int(sym + str(int(x)))
        if ans >= math.pow(2,31) or ans < -math.pow(2,31):
            return 0
        else:
            return ans