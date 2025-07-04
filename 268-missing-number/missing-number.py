class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while (i < len(nums)):
            correct = nums[i]
            if (nums[i] < len(nums) and nums[i] != nums[correct]):
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        