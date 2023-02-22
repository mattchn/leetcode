def shipWithinDays(weights, days):
   minimum = max(weights) 
   maximum = sum(weights) 
   
   while minimum < maximum:
      mid = (minimum + maximum) // 2 
      
      current_weight = 0
      required_days = 1
      for weight in weights:
         if current_weight + weight > mid:
              
               required_days += 1
               current_weight = 0
         
         current_weight += weight
      
      if required_days <= days:
         maximum = mid
      else:
         minimum = mid + 1
   
   return minimum