def fizzBuzz(n):
   """
   :type n: int
   :rtype: List[str]
   """
   result = []
   for i in range(1, n+1):
      if i % 15 == 0:
            result.append("FizzBuzz")
      elif i % 3 == 0:
            result.append("Fizz")
      elif i % 5 == 0:
            result.append("Buzz")
      else:
            result.append(str(i))
   return result

print(fizzBuzz(3))
print(fizzBuzz(15))
print(fizzBuzz(30))

   
