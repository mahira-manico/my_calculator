import colored

def display_menu():
   
   print(f"{colored.fg(177)}--Welcome to PowerCalculator!--")
   print(f"{colored.fg(199)}1. calculator")
   print(f"{colored.fg(177)}2. see history")
   print(f"{colored.fg(199)}3. remove history")
   print(f"{colored.fg(177)}Ctrl + C to quit")

def display_result(operation_result):
     print(f"{colored.fg(177)}result: {operation_result}")

def clear_screen():
  print("\033[2J\033[H", end="")