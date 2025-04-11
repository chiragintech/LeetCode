class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low1 = 0
        low2 = 0
        high1,high2 = len(nums) - 1,len(nums) - 1
        start = -1
        end = -1
        while low1 <= high1:
            mid1 = low1 + (high1 - low1) // 2
            guess1 = nums[mid1]
            if guess1 == target:
                high1 = mid1 - 1
                start = mid1
            elif target > guess1:
                low1 = mid1 + 1
            else:
                high1 = mid1 - 1
        while low2 <= high2:
            mid2 = low2 + (high2 - low2) // 2
            guess2 = nums[mid2]
            if guess2 == target:
                low2 = mid2 + 1
                end = mid2
            elif target > guess2:
                low2 = mid2 + 1
            else:
                high2 = mid2 - 1
        return [start,end]
        