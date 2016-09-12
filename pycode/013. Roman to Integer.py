class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        syms = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        val = [1, 5, 10, 50, 100, 500, 1000]

        num = 0
        for i in range(len(s)-1):
            idx1, idx2 = map(syms.index, (s[i], s[i+1]))
            if idx1 >= idx2:
                num += val[idx1]
            else:
                num -= val[idx1]
        num += val[syms.index(s[-1])]
        return num


tests = ['IV', 'III', 'II', 'V', 'VI']
for t in tests:
    print(Solution().romanToInt(t))
            

        