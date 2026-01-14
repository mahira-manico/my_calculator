
def calculator(entry_result):
 try:     
  
  a,operator,b=entry_result

  num1=float(a)
  num2=float(b)

  match operator:
      case "+":
          return num1+num2

      case "-":
          return num1-num2

      case "*":
          return num1*num2

      case "/":
          return num1/num2

      case "//":
          return num1//num2
 
      case "%":
          return num1%num2
          
      case "**":
          return num1**num2
     
      case _:
          print(f"{operator} unknow")
          return None

 except ValueError:
  print("Enter numbers only!")
  return None
  
 return entry_result

def priorities_calcul(list_entry):
 
 priorities=[
   ["**"],
   ["*", "/", "//", "%"],
   ["+", "-"]
]
 
 for group_list in priorities:
    i=0
    while i<len(list_entry):
       if list_entry[i] in group_list:
          prioritary_calcul=list_entry[i-1:i+2]
          result=calculator(prioritary_calcul)
          list_entry[i-1:i+2]=[str(result)]
          i=0
       else:
          i+=1

 return list_entry[0]





    

            