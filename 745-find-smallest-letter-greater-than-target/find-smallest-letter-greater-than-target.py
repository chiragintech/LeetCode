class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        ans = letters[0]
        high = len(letters) - 1
        while low <= high:
            mid = low + (high - low) // 2
            guess = letters[mid]
            if target < guess:
                ans = guess
                high = mid - 1
            else:
                low = mid + 1
        return ans
        