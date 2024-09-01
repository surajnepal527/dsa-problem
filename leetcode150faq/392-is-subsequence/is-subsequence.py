class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) == 0 and len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) == 0:
            return True

        cur_idx = 0
        for i in range(len(t)):
            if cur_idx < len(s) and s[cur_idx] == t[i]:
                cur_idx += 1
        
        if cur_idx == len(s):
            return True

        return False

        