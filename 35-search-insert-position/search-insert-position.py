class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low<=high:
            mid = (low + high) // 2
            guess = nums[mid]
            if target == guess:
                return mid
            elif target > guess:
                low = mid + 1
            else:
                high = mid - 1
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            
        return len(nums)