# Write a program that uses a dictionary to store information about a person, such as 
# their name, age, and favorite color. Ask the user for input and store the information in the dictionary.then,
#print the dictionary to the console
name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_color = input("Enter your favorite color: ")

my_dict = {f"name: {name}, age : {age}, favorite color: {fav_color} "}
print(my_dict)