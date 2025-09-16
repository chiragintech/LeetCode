class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0,0
        res = []
        m = len(word1)
        n = len(word2)
        while l < m and r < n:
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
        print(l, r)
        if min(m, n) == m:
            res.append(word2[r:])
        else:
            res.append(word1[l:])
        str_res = "".join(res)
        return str_res
