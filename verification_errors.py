def verification_entries(list_entry):
        if len(list_entry)<3:
            print(f"Need at least 3 arguments! {len(list_entry)} given")
            return None
        return list_entry

def is_number(value):
 try:
    float(value)
    return True
 except ValueError:
     return False
 
def is_operator(value):
 valid_operator=["**","*","/","//","%","+","-","(",")"]
 return value in valid_operator


def verification_valid_entry(list_entry):
    
   for element in list_entry:
        if not is_number(element) and not is_operator(element):
            print(f"Error! {element} is unknown.")
            return False
        
        if list_entry.count("(") != list_entry.count(")"):
            print("Error! Unbalanced parentheses.")
            return False
    
        for i in range(len(list_entry) - 1):
          if is_number(list_entry[i]) and list_entry[i+1] == "(":
            print("Error! Add "*" before '('")
            return False
            
   return True

def zero_division(list_entry):

    for i in range(len(list_entry)):
        if list_entry[i] in ["/", "//", "%"]:
            if list_entry[i+1]=="0":
                print(f"Error! {list_entry[i+1]} cannot divide by zero! ")
                return False
    return True



def verify_all(list_entry):

    if not verification_entries(list_entry):
        return False
    if not verification_valid_entry(list_entry):
        return False
    if not zero_division(list_entry):
        return False
    return True          

     


        