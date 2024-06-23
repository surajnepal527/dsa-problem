class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = ""
        i = n - 1
        while i >= 0:

            while i>=0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            end = i
            while i>= 0 and s[i] != ' ':
                i -= 1
            start = i + 1

            word = s[start: end+1]

            if result:
                result += " " + word
            else:
                result = word
            
        return result
        