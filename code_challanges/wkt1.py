#  Write a program that accepts user input to create a list of integers. Then,
#  compute the sum of all the integers in the list
nums = input("Enter list elements separated by space: ")

list_1 = nums.split() 

total = 0

for x in list_1:
  total += int(x)
print(f'the sum of numbers in the list is : {total}')