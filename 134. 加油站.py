class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        _len = len(gas)
        for idx1,g in enumerate(gas):
            if g == 0 or gas[idx1]-cost[idx1]<0 or sum(gas[:idx1+1])<cost[idx1]:
                continue
            cur = 0
            for idx2 in range(_len):
                cur += gas[(idx1 + idx2) % _len]
                cur -= cost[(idx1 + idx2) % _len]
                if cur < 0:
                    break
                print(f"+{gas[(idx1 + idx2) % _len]}-{cost[(idx1 + idx2) % _len]}",end='')
                # print(cur,end=' ')
            if cur >= 0:
                return idx1

        return -1


s = Solution()
print(s.canCompleteCircuit2([1,2,3,4,5],[3,4,5,1,2]))
print(s.canCompleteCircuit2([3,1,1],[1,2,2]))
print(s.canCompleteCircuit2([2,3,4],[3,4,3]))
print(s.canCompleteCircuit2([1,2,3,4,5,5,70],[2,3,4,3,9,6,2]))
