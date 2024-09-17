class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashset = {}
        i , j, n  = 0, 0 , len(s)
        ans = 0
        while i <= j and j < n:
            hashset[s[j]] = hashset.get(s[j],0) + 1
            most_freq_count = self.getMostFrequentChar(hashset)
            if j-i+1 - most_freq_count <= k:
                ans = max(ans, j-i+1)
                j += 1
            else:
                hashset[s[i]] = hashset.get(s[i]) - 1
                hashset[s[j]] = hashset.get(s[j],0) - 1
                i += 1

        return ans
        


    

    def getMostFrequentChar(self, hashset):
        most_freq_count = 0
        for key, value in hashset.items():
            most_freq_count = max(most_freq_count,value)
        return most_freq_count