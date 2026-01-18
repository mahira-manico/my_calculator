
from functions import *
from display import *
from history import *
from verification_errors import *
import time
import colored

def menu_core():
 
 clear_screen()
 while True:
  clear_screen()
  try:
   
    display_menu()
    redirection=int(input(f"{colored.fg(199)}what do you want to do?: "))
   
    if redirection not in range(1,4):
     print("Please enter 1, 2 or 3")
     time.sleep(1)
     continue

    if not redirection:
     continue

    match redirection:

     case 1:
      while True:
       
       clear_screen()
       entry=input(f"{colored.fg(5)}enter your operation: ")        
        
       if not entry.strip():
        print("please enter an operation!")
        continue
       
       user_entry=parsing(entry)

       if not verify_all(user_entry):
        time.sleep(1)
        continue
       
       user_entry=parentheses(user_entry)
       
       calculator_result=priorities_calcul(user_entry)

       if calculator_result is None:
        continue
       
       if save_history(entry, calculator_result):
        print("Calcul saved to history")
       
       display_result(calculator_result)

       retry_op=input(f"{colored.fg(5)}do you want to try again?(y/n)").lower()
       if retry_op=="y":
        continue
       else:
        print(f"{colored.fg(177)}returning to menu..")
        time.sleep(1)
        break


     case 2:
      clear_screen
      while True:
       display_history()
       stay=input(f"{colored.fg(5)}tap menu to quit: ").lower()
       if stay=="menu":
        break
 
     case 3:
      remove_history()

  except ValueError:
   print("Please enter a number!")
   time.sleep(1)
  except KeyboardInterrupt:
   print(f"{colored.fg(177)}Goodbye!")
   time.sleep(1)
   break
 clear_screen()
 