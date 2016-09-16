class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_bull = 0
        num_cows_s = {}
        num_cows_g = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_bull += 1
            else:
                num_cows_s[secret[i]] = num_cows_s.get(secret[i],0) + 1
                num_cows_g[guess[i]] = num_cows_g.get(guess[i], 0) + 1
        num_cow = 0
        for item in num_cows_s:
            if item in num_cows_g:
                num_cow += min(num_cows_g[item], num_cows_s[item])
        return str(num_bull)+'A'+str(num_cow)+'B'
