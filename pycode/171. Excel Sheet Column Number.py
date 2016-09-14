class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method 1
        # def to_digits(c):
        #     return ord(c.upper())-ord('A')+1
        # base = 1
        # ret = 0
        # for i,c in enumerate(reversed(s)):
        #     ret += base*to_digits(c)
        #     base *= 26
        # return ret

        # method 2
        from functools import reduce
        return reduce(lambda x,y: x*26+y, map(lambda x:ord(x)-64, s))

print(Solution().titleToNumber('AA'))
        
