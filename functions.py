
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

def parsing(list_entry):
   text=list_entry.replace(" ", "")
   final_list=[]
   current_number=""
   i=0
   operators=["**","//","*","%","/","-","+","(", ")"]
   while i<len(text):
      
      if text[i]== "-" and (i==0 or text[i-1] in "+-*/%"):
            current_number+=text[i]
            i += 1
            if i >= len(text): break

      if text[i].isdigit() or text[i]==".":
           current_number+=text[i]
           i+=1
      
      else:
         
         if current_number:
            final_list.append(current_number)
            current_number=""
        
         if text[i] in "()":
            final_list.append(text[i])
            i+=1
         
         elif i + 1 < len(text) and  text[i:i+2] in ["**","//"]:
            final_list.append(text[i:i+2])
            i+=2

         elif text[i] in operators:
            final_list.append(text[i])
            i+=1
         else:
            final_list.append(text[i])
            i+=1
        
   if current_number:
      final_list.append(current_number)
   return final_list

def parentheses(entry_result):
   
   while "(" in entry_result:
      start=-1
      end=-1

      for i in range(len(entry_result)):
       if entry_result[i]=="(":
          start=i

       if entry_result[i]==")" and start!=-i:
          end=i
          break
      if start != -1 and end != -1:
       sub_calcul=entry_result[start+1:end]
       result=priorities_calcul(sub_calcul)
       entry_result[start:end+1]=[str(result)]

      else:
       break
      
   return entry_result