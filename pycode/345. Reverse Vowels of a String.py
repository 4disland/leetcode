class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [v for v in reversed(s) if v in 'aoieuAOIEU']
        j = 0
        ret = list(s)
        for i in range(len(ret)):
            if ret[i] in vowels:
                ret[i] = vowels[j]
                j += 1
        return ''.join(ret)

print(Solution().reverseVowels('leetcode'))

