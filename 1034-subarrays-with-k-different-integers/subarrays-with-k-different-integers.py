
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(x):
            l = 0
            h = {}
            count = 0
            for r in range(len(nums)):
                h[nums[r]] = h.get(nums[r], 0) + 1
                while len(h) > x:
                    h[nums[l]] -= 1
                    if h[nums[l]] == 0:
                        h.pop(nums[l])
                    l += 1
                count += (r - l + 1)
            return count
        
        return helper(k) - helper(k - 1)
