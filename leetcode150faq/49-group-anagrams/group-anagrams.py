from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            freq_array = [0]*26
            for ch in s:
                freq_array[ord(ch) - ord('a')] += 1
            anagramMap[tuple(freq_array)].append(s)
        return list(anagramMap.values())



        