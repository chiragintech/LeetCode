class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sorted nums
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            guess = nums[mid]
            if (target == guess):
                return mid
            elif (target > guess):
                low = mid + 1
            else:
                high = mid - 1
        return -1