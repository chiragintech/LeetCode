class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cu_sum = 0
        d = {0:-1}
        for i, num in enumerate(nums):
            cu_sum += num
            rem = cu_sum % k
            if rem in d:
                prev = d[rem]
                if i - prev >= 2:
                    return True
            else:
                d[rem] = i
        return False
                

