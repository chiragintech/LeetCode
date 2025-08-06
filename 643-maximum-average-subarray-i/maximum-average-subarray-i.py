class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = round(window_sum / k, 5)
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_avg = max(max_avg, round(window_sum / k,5))
        return max_avg
