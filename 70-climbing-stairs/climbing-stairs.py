def memo(n, dp):
    if n == 0 or n == 1:
        return 1 # return 1 when you are counting number of ways
    # l = memo(n-1, dp)
    # r = memo(n-2, dp)
    # return l + r
    dp[n] = memo(n-1, dp) + memo(n-2,dp)
    return dp[n]
def tab(n, dp):
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[n] = tab(n-1,dp) + tab(n-2,dp)
    return dp[n]
def optim(n, dp):
    prev2 = 1
    prev = 1
    for i in range(2, n + 1):
        curi = prev + prev2
        prev2 = prev
        prev = curi
    return prev
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        count = optim(n, dp)
        return count