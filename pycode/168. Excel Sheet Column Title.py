class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n:
            r = (n-1)%26
            s = chr(ord('A')+r) + s
            n = (n-1)//26
        return s