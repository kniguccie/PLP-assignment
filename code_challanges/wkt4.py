# Write a program that accepts user input to create two sets of integers. Then,
#  create a new set that contains only the elements that are common to both sets

num_1 = (input("Enter list elements separated by space: "))
num_2 = (input("Enter list elements separated by space: "))

list_1 = num_1.split()
list_2 = num_2.split()

set1 = set(list_1)
set2 = set(list_2)

set3 = set1 & set2
print(set3)

