class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # true if atleast twice in array
        # false if every element distinct
        nums.sort()
        unique = list(set(nums))
        unique.sort()
        print(nums)
        print(unique)
        if unique == nums:
            return False
        return True