class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        length = 0
        h = {}
        max_len = 0
        print(s)
        n = len(s)
        while l < n and r < n:
            if s[r] not in h:
                h[s[r]] = 1
                r += 1
            else:
                l += 1
                r = l + 1
                if l < n:
                    h = {s[l]:1}
            max_len = max(r-l, max_len)
        return max_len


