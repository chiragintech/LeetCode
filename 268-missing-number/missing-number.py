class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while (i < len(nums)):
            correct = nums[i] - 1
            if (nums[i] != nums[correct] and (correct >= 0 and correct < len(nums))):
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return 0