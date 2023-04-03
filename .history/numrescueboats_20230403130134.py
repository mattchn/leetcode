def numRescueBoats(people, limit):
   # if weight of max person is over limit
   if max(people) > limit:
      return -1
   
   if sum(people) <= limit:
      return 1
   
   