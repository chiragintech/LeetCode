class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        h = {'a':0,'b':0,'c':0}
        r = 0
        flag = 0
        for r in range(len(s)):
            h[s[r]] += 1
            while h['a'] >=1 and  h['b'] >= 1 and h['c'] >= 1:
                count += 1
                count += (len(s) - 1 - r)
                h[s[l]] -= 1
                l += 1
        return count
            


