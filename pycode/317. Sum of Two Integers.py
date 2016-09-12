class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        for _ in range(32):
            a, b = a^b, (a&b) << 1
        return a if a & 0x80000000 else a & 0xffffffff
# https://discuss.leetcode.com/topic/50315/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
print(Solution().getSum(12,15))