def intToRoman(num):
   values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
   
   symbols = [
      "M", "CM", "D", "CD",
      "C", "XC", "L", "XL",
      "X", "IX", "V", "IV",
      "I"
      ]
   
   roman = ''
   
   for i, val in enumerate(values):
      while num >= val:
         num -= val
         roman += symbols[i]
   return roman