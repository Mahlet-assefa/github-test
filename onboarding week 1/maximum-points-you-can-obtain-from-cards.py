class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result = float("inf")
        total=0
        l=0
        curr=0
        for r, point in enumerate(cardPoints):
            total += point
            curr += point
            if r-l+1 > len(cardPoints)-k:
                curr -= cardPoints[l]
                l += 1
            if r-l+1 == len(cardPoints)-k:
                result = min(result, curr)
        return total-result