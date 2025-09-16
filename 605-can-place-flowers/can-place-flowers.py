class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        def isSafe(k):
            if flowerbed[k-1] == 0 and flowerbed[k] == 0 and flowerbed[k+1] == 0:
                return True
            return False
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if isSafe(i):
                flowerbed[i] = 1
                count += 1
        return count >= n