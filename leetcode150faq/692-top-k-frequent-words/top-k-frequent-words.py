from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #step1 user Counter to generate freqency map
        freq_count = Counter(words)
        #step2 use sorting by freq of word in descending and word itself by ascending
        candidates = sorted(freq_count, key=lambda word:(-freq_count[word],word))
        #return first k item
        return candidates[:k]
        