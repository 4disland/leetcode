class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        a, b = 2, 1
        for _ in range(n-2):
            a, b = a+b, a
        return a
        