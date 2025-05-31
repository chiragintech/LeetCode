class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # count = 0
        # for i in range(len(g)):
        #     for j in range(len(s)):
        #         if s[j] >= g[i]:
        #             count+=1
        #             break
        # return count
        g.sort()
        s.sort()
        l = 0
        r = 0
        count = 0
        while l != len(s) and r != len(g):
            if s[l] >= g[r]:
                count +=1
                r += 1
                l += 1
            else:
                l += 1
        return count