class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1 and digits[0] < 9:
            return [digits[0]+1]
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]
        num = reduce(lambda x,y:10*x+y, digits)
        
        return [int(i) for i in str(num+1)]
        