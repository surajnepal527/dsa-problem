from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_counter = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_counter:
                    seen[word] += 1
                    count += 1

                    while seen[word] > word_counter[word]:
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)
                else:
                    seen = Counter()
                    count = 0
                    left = j + word_len

        return result
