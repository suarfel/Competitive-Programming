class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens)-1
        score, result = 0, 0
        while i <= j:
            if tokens[i] <= power:
                power-=tokens[i]
                score+=1
                result = max(score, result)
                i+=1
            elif score >= 1:
                power+=tokens[j]
                score-=1
                j-=1
            else:
                break
        return result