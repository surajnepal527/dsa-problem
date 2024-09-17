class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        #initialize the frequency map
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for r in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            #incremented on right side
            s2_count[ord(s2[r]) - ord('a')] += 1
            #decremented on left side
            s2_count[ord(s2[r-len(s1)])- ord('a')] -= 1

        
        return s1_count == s2_count

            