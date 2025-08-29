class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = defaultdict(int)
        for c in magazine:
            magazine_map[c] += 1
        for ran_char in ransomNote:
            if magazine_map[ran_char] <= 0:
                return False
            magazine_map[ran_char] -= 1
        return True