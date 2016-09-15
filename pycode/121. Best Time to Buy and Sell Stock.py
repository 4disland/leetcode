class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minv = 0xffffffff
        maxp = 0
        for i in prices:
            minv = min(minv, i)
            maxp = max(maxp, i-minv)
        return maxp