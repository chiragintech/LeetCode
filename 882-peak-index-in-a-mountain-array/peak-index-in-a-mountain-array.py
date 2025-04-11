class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def get(arr, pos):
            return arr[pos] if pos < len(arr) else float('inf')

        low = 0
        ans = -1
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            guess = arr[mid]
            if guess > get(arr, mid + 1):
                high = mid - 1
                ans = mid
            elif guess < get(arr, mid + 1):
                low = mid + 1
        return ans