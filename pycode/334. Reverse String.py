class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        s = list(s)
        for i in range(len(s)//2):
            s[i],s[~i] = s[~i], s[i]
        return ''.join(s)