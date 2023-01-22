def canPlaceFlower(flowerbed, n):
   numOfOnes = flowerbed.count(1)
   return (n <= numOfOnes/2)