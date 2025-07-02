def helper(index,sign,result,started,s):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if index == len(s):
        return sign * result
    ch = s[index]
    if not started:
        if ch == ' ':
            return helper(index + 1, sign, result, False,s)
        elif ch == '-':
            return helper(index + 1, -1, result, True,s)
        elif ch == '+':
            return helper(index + 1, 1, result, True,s)
        elif ch.isdigit():
            return helper(index + 1, sign, int(ch), True,s)
        else:
            return 0
    else:
        if ch.isdigit():
            digit = int(ch)
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            return helper(index + 1, sign, result * 10 + digit, True,s)
        else:
            return sign * result
class Solution:
    def myAtoi(self, s: str) -> int:
        return helper(0, 1, 0, False,s)
