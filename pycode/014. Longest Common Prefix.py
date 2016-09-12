class Solution(object):
    def allSame(self, strs, j):
        c = strs[0][j]
        for i in range(1, len(strs)):
            if strs[i][j] != c:
                return False
        return True

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not all(strs):
            return ''
        ret = ''
        for i in range(min(map(len, strs))): # min() arg can't be empty seq'
            if self.allSame(strs, i):
                ret += strs[0][i]
            else:
                break
        return ret

tests = ['a']
print(Solution().longestCommonPrefix(tests))
