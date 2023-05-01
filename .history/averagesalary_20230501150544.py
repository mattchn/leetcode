def average(salary):
   salary.sort()
   salary.pop(0)
   salary.pop(-1)
   sum_of_salary = sum(salary)
   
   return sum_of_salary/(len(salary))