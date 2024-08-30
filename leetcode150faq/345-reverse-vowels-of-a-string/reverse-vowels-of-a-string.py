class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o','u','A', 'E','I', 'O', 'U'}
        left = 0
        right = len(s) - 1
        chars = list(s)
        while left < right:
            left_vowel = chars[left] in vowels
            right_vowel =chars[right] in vowels
            if left_vowel and right_vowel:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            elif left_vowel:
                right -= 1
            elif right_vowel:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(chars)
