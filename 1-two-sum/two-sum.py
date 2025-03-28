class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums - array, target - int
        # return indices of the 2 numbers to add up to target
        # the same element you cannot use twice
        index = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
        return index