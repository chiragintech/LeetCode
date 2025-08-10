class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        max_count = 0 
        h = {0:0,1:0}
        n = len(nums)
        r = 0
        for r in range(n):
            h[nums[r]] += 1
            while h[0] > k:
                h[nums[l]] -= 1
                l += 1
            max_count = max(max_count, r-l+1)
        return max_count
            