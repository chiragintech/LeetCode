class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = defaultdict(int)
        for i in range(len(nums)):
            h[nums[i]] += 1
        if max(h.values()) > 1:
            return True
        return False