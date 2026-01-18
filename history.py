import time
import colored

def save_history(entry, calculator_result):
  with open("history.txt", "a") as fichier:
   fichier.write(f"{entry}={calculator_result}\n")
        
def display_history():
 try:
   with open("history.txt", "r") as fichier:
      data = fichier.read()
      if not data.strip():
       print("Empty history!")
      else:
       print(f"{colored.fg(177)}--Calculs history--\n")
       print(f"{colored.fg(199)}",data)
 
 except FileNotFoundError:
    print("History empty, no files found")

def remove_history():
 while True:
   remove_history=input(f"{colored.fg(177)}Remove history? (y/n)").lower()
   if remove_history=="y":
      with open("history.txt", "w"):
       print(f"{colored.fg(199)}History have been reinitialized")
       time.sleep(1)
       pass
       break
   else:
        print(f"{colored.fg(199)}History not deleted")
        time.sleep(1)
        break
        