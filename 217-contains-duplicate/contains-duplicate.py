class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # true if atleast twice in array
        # false if every element distinct
        return len(set(nums)) < len(nums) #if nums is more, it is going to return true