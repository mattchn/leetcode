def numRescueBoats(people, limit):
   # base cases
   if max(people) > limit:
      return -1
   if sum(people) <= limit:
      return 1
   
   # sort people by weight
   people.sort()
   
   # initialize variables
   start = 0
   end = len(people) - 1
   boats = 0
   
   while start <= end:
      if people[start] + people[end] <= limit:
         start += 1
         end -= 1
         boats += 1
      
   return boats
   
   