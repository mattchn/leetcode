num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3

new_num1 = num1[:m]
new_num2 = num2[:n]
merge = new_num1 + new_num2
merge.sort()
print(merge)