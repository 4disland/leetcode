class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        def to_digits(c):
            return ord(c.upper())-ord('A')+1
        base = 1
        ret = 0
        for i,c in enumerate(reversed(s)):
            ret += base*to_digits(c)
            base *= 26

        return ret
