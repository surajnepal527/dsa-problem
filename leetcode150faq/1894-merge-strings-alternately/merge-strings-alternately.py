class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1=w2=0
        n1 = len(word1)
        n2 = len(word2)
        ans = []
        while w1 < n1 and w2 <  n2:
            ans.extend([word1[w1], word2[w2]])
            w1 += 1
            w2 += 1
        
        if w1 < n1:
            ans.extend(word1[w1:n1])
        if w2 < n2:
            ans.extend(word2[w2:n2])
        
        return "".join(ans)
