class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        freq_word1 = [0] * 26
        freq_word2 = [0] * 26
        for w1 in word1:
            index = ord(w1) - ord('a')
            freq_word1[index] += 1
        
        for w2 in word2:
            index = ord(w2) - ord('a')
            freq_word2[index]  += 1

        return sorted(freq_word1) == sorted(freq_word2)
        
        # freq_map = {}
        # for f1 in freq_word1:
        #     freq_map[f1] = freq_map.get(f1, 0) + 1

        # for f2 in freq_word2:
        #     if f2 not in freq_map:
        #         return False
        #     else: 
        #         freq_map[f2] = freq_map.get(f2) - 1
        
        # for value in freq_map.values():
        #     if value > 0:
        #         return False
        
        # return True
        