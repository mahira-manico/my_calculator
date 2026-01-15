def display_menu():
   
   print("--Welcome to PowerCalculator!--")
   print("1. calculator")
   print("2. see history")
   print("3. remove history")
   print("Ctrl + C to quit")

def display_result(operation_result):
     print(f"result: {operation_result}")

def clear_screen():
  print("\033[2J\033[H", end="")