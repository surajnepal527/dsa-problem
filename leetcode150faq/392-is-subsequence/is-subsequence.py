class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False

        i = 0
        m = 0
        while m < len(t):
            if t[m] == s[i]:
                i += 1
            if i == len(s):
                return True
            m += 1
        
        return False
            