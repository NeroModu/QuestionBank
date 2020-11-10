class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) < 3:
            if 1 in flowerbed:
                return n == 0
            else:
                return n <= 1
        
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            
        return n == 0
