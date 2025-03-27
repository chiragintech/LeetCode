class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # true if atleast twice in array
        # false if every element distinct
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False