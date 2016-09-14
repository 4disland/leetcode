class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in s:
             t = t.replace(c, '', 1) # only remove the first c in t
        return t

a = Solution().findTheDifference('abcd', 'dcabe')
print(a)