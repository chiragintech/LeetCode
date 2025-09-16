class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        if min(m, n) == m:
            min_str = str1
            max_str = str2
        else:
            min_str = str2
            max_str = str1
        def find_gcd(m, n):
            if m == n:
                return m
            elif m > n:
                return find_gcd(m - n, n)
            else:
                return find_gcd(m, n-m)
        if len(max_str) % len(min_str) == 0:
            if min_str * (len(max_str) // len(min_str)) == max_str:
                return min_str
            else:
                return ""
        else:
            g = find_gcd(len(min_str), len(max_str))
            print(g)
            if min_str[:g] * (len(min_str) // g) == min_str and min_str[:g] * (len(max_str) // g) == max_str:
                return min_str[:g]
            else:
                return ""
