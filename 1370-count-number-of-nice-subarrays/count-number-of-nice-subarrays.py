class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            h = {'odd':0}
            l = 0
            count = 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    h['odd'] += 1
                while h['odd'] > x:
                    if nums[l] % 2 == 1:
                        h['odd'] -= 1
                    l += 1
                count += (r-l+1)
            return count
        return helper(k) - helper(k-1)
    