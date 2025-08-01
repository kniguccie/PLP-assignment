# Name Nigussie Desalegn
# this is basic calculator assignment
try:

  num1 = int(input("Enter the first number:"))
  num2 = int(input("Enter the second number:"))
  mathsOperator = input("mathematical operator:")

  if mathsOperator == "+":
    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is {sum}")
  elif mathsOperator == "-":
    difference = num1 - num2
    print(f"the difference of {num1} and {num2} is {difference}")
  elif mathsOperator == "*":
    product = num1 * num2
    print(f"the product of {num1} and {num2} is {product}")
  else:
    quotient = num1 / num2
    print(f"the quotient of {num1} and {num2} is {quotient}")

except ZeroDivisionError:
  print("Undefined operation")


