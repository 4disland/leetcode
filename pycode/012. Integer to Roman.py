class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        ret = ''
        for k in range(len(v)):
            ret = ret + num//v[k]*sym[k]
            num = num%v[k]
        return ret

test = [9]
print(map(Solution().intToRoman, test))