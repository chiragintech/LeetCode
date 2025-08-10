class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        h = collections.defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(nums)):
            h[nums[r]] += 1
            while h[nums[r]] > k:
                h[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
