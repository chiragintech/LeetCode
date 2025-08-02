class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        count = 0
        cu_sum = 0
        for num in nums:
            cu_sum += num
            complement = cu_sum - k
            if complement in d:
                count += d[complement]
            d[cu_sum] = d.get(cu_sum, 0) + 1
        return count