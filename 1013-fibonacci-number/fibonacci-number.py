def helper(n): 
    if n == 0 or n == 1:
        return n
    return helper(n-1) + helper(n-2)
class Solution:
    def fib(self, n: int) -> int:
        return helper(n)
        