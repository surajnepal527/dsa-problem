class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        n = len(tokens)
        tokens.sort()
        cur_score = 0
        i, j = 0 , n-1
        while i <= j:
            if power >= tokens[i]:
                cur_score += 1
                power -= tokens[i]
                max_score = max(max_score, cur_score)
                i += 1
            elif cur_score >= 1:
                power += tokens[j]
                cur_score -= 1
                j -= 1
            else:
                break
        return max_score


        