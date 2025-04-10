# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            g = mid + 1
            if guess(g) == 0:
                return g
            elif guess(g) == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1 
