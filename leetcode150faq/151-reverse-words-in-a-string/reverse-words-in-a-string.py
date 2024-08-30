class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        start = 0
        end = len(words) - 1
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -=1
        
        return " ".join(words)