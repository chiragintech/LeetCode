class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        dp = [[float(-inf)] * (k + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = nums[0] * k
        for i in range(1, len(nums)):
            dp[i][0] = max({nums[i]*k, dp[i-1][0] + nums[i]*k})
        for j in range(1, k):
            currk = k - j
            if currk % 2 == 0:
                sign = -1
            else:
                sign = 1
            for i in range(j, len(nums)):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i] * currk * sign
        maxStrength = float('-inf')
        for i in range(len(nums)):
            maxStrength = max(maxStrength, dp[i][k-1])
        return maxStrength