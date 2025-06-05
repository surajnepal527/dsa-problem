from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for s in strs:
            freq_map = [0]*26
            for ch in s:
                freq_map[ord(ch)-ord('a')] += 1
            ana_map[tuple(freq_map)].append(s)
        return list(ana_map.values())
        