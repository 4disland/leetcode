class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # method 1
        # for c in s:
        #      t = t.replace(c, '', 1) # only remove the first c in t
        # return t

        # method 2
        for c in s+t:
            if (s+t).count(c) % 2:
                return c

        # method 3
        # code = 0
        # for c in s+t:
        #     code ^= ord(c)
        # return chr(code)
        

a = Solution().findTheDifference('abcd', 'dcabe')
print(a)