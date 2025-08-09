class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sum of the points taken - maximum sum
        n = len(cardPoints)
        window = sum(cardPoints[:k])
        max_sum = window
        for i in range(1,k + 1):
            window = window - cardPoints[k-i] + cardPoints[n-i]
            max_sum = max(window, max_sum)
        return max_sum
            
        