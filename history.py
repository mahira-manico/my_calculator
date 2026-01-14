import time

def save_history(entry, calculator_result):
  with open("history.txt", "a") as fichier:
   fichier.write(f"{entry}={calculator_result}\n")
        
def display_history():
 try:
   with open("history.txt", "r") as fichier:
      print("--Calculs history--\n")
      for content in fichier:
       if not content:
         print("Empty history!")
       else:
         print(content)
      
 except FileNotFoundError:
    print("History empty, no files found")

def remove_history():
 while True:
   remove_history=input("Remove history? (y/n)").lower()
   if remove_history=="y":
      with open("history.txt", "w"):
       print("History have been reinitialized")
       time.sleep(1)
       pass
       break
   else:
        print("History not deleted")
        time.sleep(1)
        break
        