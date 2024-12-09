class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        char_map = [0]*26
        for ch in chars:
            idx =  ord(ch) - ord('a')
            char_map[idx] += 1
        for word in words:
            word_map = [0] *26
            for ch in word:
                idx = ord(ch) - ord('a')
                word_map[idx] += 1
            goodWord = True
            for i in range(26):
                if word_map[i] > char_map[i]:
                    goodWord = False
                    break
            if goodWord:
                result += len(word)
        return result

                
                    

        