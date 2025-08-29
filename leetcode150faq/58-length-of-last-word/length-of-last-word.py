class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         clean_text = ' '.join(s.split())
         words = clean_text.split()
         words_len = len(words)
         return len(words[words_len -1])

        