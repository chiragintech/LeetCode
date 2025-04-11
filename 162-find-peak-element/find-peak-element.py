class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        def get(arr, pos):
            return arr[pos] if pos < len(arr) else float('inf')
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > get(arr,mid + 1):
                end = mid
            else:
                start = mid + 1

        return start