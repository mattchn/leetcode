def countAndSay(n):
   if n == 1:
      return "1"
   
   # recursivly generate previous term in sequence
   prev_term = countAndSay(n - 1)
   
   current_digit = prev_term[0]
   current_count = 0
   result = ""
   
   # iterate through previous term and generate current term
   for digit in prev_term:
      if digit == current_digit:
         current_count += 1
      
      else:
         result += str(current_count) + current_digit
         current_digit = digit
         current_count = 1
      
   # add the last set of digits to result
   result += str(current_count) + current_digit
   
   return result