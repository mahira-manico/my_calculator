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
 valid_operator=["**","*","/","//","%","+","-"]
 return value in valid_operator


def verification_valid_entry(list_entry):
    
    if not is_number(list_entry[0]):
         print("Must start with a number")
         return False
    else:
        if not is_number(list_entry[-1]):
         print("Must end with a number")
         return False
    
    for i in range(len(list_entry)):
        elements_in_list=list_entry[i]
        if i%2==0:
            if not is_number(elements_in_list):
                print("Incorrect position! must be a number")
                return False
        else:
            if not is_operator:
                print("Incorrect position! Must be an operator")
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

     


        