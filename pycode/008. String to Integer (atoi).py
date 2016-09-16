class Solution(object):
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        p = re.compile(r'^[+-]?[0-9]+')
        m = re.match(p, str.strip())
        if m:
            ret = int(m.group())
            if ret < -0x80000000:
                return -0x8000000
            elif ret > 0x7fffffff:
                return 0x7fffffff
            return ret
        else:
            return 0
        
print(Solution().myAtoi('-2147483649'))