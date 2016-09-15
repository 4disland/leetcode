class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if not num&(num-1) and num&0x55555555:
            return True
        else:
            return False

        # could write in one line
        # return num > 0 and num&(num-1)!=0 and num&0x55555555
        