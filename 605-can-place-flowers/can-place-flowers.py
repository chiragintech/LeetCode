class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        def isSafe(k):
            if flowerbed[k] == 1:
                return False
            if len(flowerbed) == 1:
                return True
            if k == 0:
                if flowerbed[k+1] != 1:
                    return True
                else:
                    return False
            if k == len(flowerbed) - 1:
                if flowerbed[k-1] != 1:
                    return True
                else:
                    return False
            if flowerbed[k-1] == 0 and flowerbed[k+1] == 0 and flowerbed[k-1] == 0: 
                return True
            return False
            
        for i in range(len(flowerbed)):
            if isSafe(i):
                flowerbed[i] = 1
                count += 1
        return count >= n