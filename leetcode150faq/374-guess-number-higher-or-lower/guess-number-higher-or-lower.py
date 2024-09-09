# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left , right = 1, n
        while left <= right:
            guess_num = (left+right)/2
            val = guess(guess_num)
            if val == 0:
                return guess_num
            elif val == -1:
                right = guess_num - 1
            else:
                left = guess_num + 1
        
        return -1


        