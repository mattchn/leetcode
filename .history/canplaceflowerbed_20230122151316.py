def canPlaceFlower(flowerbed, n):
   numOfZeros = flowerbed.count(0)
   
   return (n <= numOfZeros/2)