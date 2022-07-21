# Calculator app cause why not. Does simple +-*/
# Ints only, the bouncer is checking IDs

from art import logo

def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def mult(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2

operations = {"+": add,
             "-": sub,
             "*": mult,
             "/": div}


print(logo)

num1 = int(input("First Number: "))


keep_on_calculating = True

while keep_on_calculating == True:
  print("")
  for op_keys in operations.keys():
    print(op_keys)

  user_operation = input("\nPick an operation from the list: ")

  num2 = int(input(f"\nNext Number: \n{num1} {user_operation} :"))
  
  answer = operations[user_operation](num1, num2)
  # answer = the user input 'user_operation' and then it looks at the operations dict to see what function to pass num1 and num2 into
  
  print(f"\n{num1} {user_operation} {num2} = {answer}")

  keep_on_calculating_str = input("Wanna keep calculating with the answer?? \nY or N").upper()
  if keep_on_calculating_str == "Y":
    keep_on_calculating = True
  else:
    print(f"Final Answer is {answer}")
    keep_on_calculating = False

  num1 = answer
  