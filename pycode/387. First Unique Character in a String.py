class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        amap = {}
        for c in s:
            amap[c] = amap.get(c,0) + 1
        for i,c in enumerate(s):
            if amap[c] == 1:
                return i
        return -1