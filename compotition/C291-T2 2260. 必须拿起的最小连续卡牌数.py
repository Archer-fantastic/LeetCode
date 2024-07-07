class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        if len(cards) == len(set(cards)):
            return -1
        dic = {}
        min_len = len(cards)
        for idx,card in enumerate(cards):

            if card in dic and idx - dic[card] + 1 < min_len:
                min_len = idx - dic[card] + 1
                dic[card] = idx
            dic[card] = idx
        return min_len