def square(n):
    ans = 0
    while n > 0:
        x = n % 10
        ans += x*x
        n = n // 10
    return ans
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = square(n)
        fast = square(square(n))
        if slow == 1 or fast == 1:
            return True
        while slow != fast:
            slow = square(slow)
            fast = square(square(fast))  
            if slow == 1 or fast == 1:
                return True
        return False      