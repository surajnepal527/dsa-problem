class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        res = []
        for s in strs:
            freq_array = [0]*26
            for ch in s:
                idx = ord(ch) - ord('a')
                freq_array[idx] += 1
            freq_tuple = tuple(freq_array)
            if freq_tuple in anagramMap:
                anagramMap[freq_tuple].append(s)
            else:
                anagramMap[freq_tuple] = [s]
        return list(anagramMap.values())



        