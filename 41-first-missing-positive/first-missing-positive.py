class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while (i < len(nums)):
            correct = nums[i] - 1
            if (nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]):
                nums[i],nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1