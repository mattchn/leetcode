def compress(chars):
   read_index, write_index = 0, 0
   count = 1
   
   for i in range(len(chars)):
      if i < len(chars) - 1 and chars[i] == chars[i+1]:
         count += 1
      else:
         chars[write_index] = chars[read_index]
         write_index += 1
         if count > 1:
            for digit in str(count):
               chars[write_index] = digit
               write_index += 1
         count = 1
      read_index += 1
   
   return write_index