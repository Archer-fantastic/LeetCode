class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        exchange = numExchange
        res = 0

        while not (full == 0 and empty < exchange):
            res += full
            empty += full
            full = 0
            while empty >= exchange:
                empty -= exchange
                full += 1
                exchange += 1

        return res