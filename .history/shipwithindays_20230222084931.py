def shipWithinDays(weights, days):
   minimum_days = max(weights) 
   maximum_days = sum(weights) 
   
   while minimum_days < maximum_days:
      mid = (minimum_days + maximum_days) // 2 
      
      current_weight = 0
      required_days = 1
      for weight in weights:
         if current_weight + weight > mid:
              
               required_days += 1
               current_weight = 0
         
         current_weight += weight
      
      if required_days <= days:
         maximum_days = mid
      else:
         minimum_days = mid + 1
   
   return minimum_days