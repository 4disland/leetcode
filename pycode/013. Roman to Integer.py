class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        syms = [I, V, X, L, C, D, M]
        val = [1, 5, 10, 50, 100, 500, 1000]

        num = 0
        