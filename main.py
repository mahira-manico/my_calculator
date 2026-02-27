from menu_core import menu_core
import os
import colored
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{colored.fg(199)}🚀 WELCOME IN POWER CACLULATOR")
print("-" * 30)
if __name__=="__main__":
  menu_core()