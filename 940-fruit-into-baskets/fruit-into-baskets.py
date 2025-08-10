class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = {}
        l = 0
        max_len = 0
        for r in range(len(fruits)):
            if fruits[r] not in h:
                h[fruits[r]] = 1
            else:
                h[fruits[r]] += 1
            print(h)
            while len(h) > 2:
                if h[fruits[l]] - 1 == 0:
                    del h[fruits[l]]
                else:
                    h[fruits[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
            