class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        n2 = n
        if n2 < 0:
            n2 = -1 * n2
        while n2:
            if n2 % 2:
                ans = ans * x
                n2 = n2 - 1
            else:
                x = x * x
                n2 = n2 // 2
        if n < 0:
            ans = 1.0 / ans
        return ans
        
        