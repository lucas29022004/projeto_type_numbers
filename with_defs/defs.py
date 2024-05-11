import vars, os

#----------------------hexadecimal---------------------------------------------------    
def convert_decimal_to_hexadecimal(number):
    return hex(number)

def convert_hexadecimal_to_binario(number):
    return bin(int(number, 16))[2:] 

def convert_hexadecimal_to_octal(number):
    return oct(int(number, 16))[2:]  

def convert_hexadecimal_to_decimal(number):
    return int(number, 16)

#---------------------octal---------------------------------
def convert_decimal_to_octal(number):
    return oct(number)

def octal_para_hexadecimal(number):
    return hex(int(number, 8))[2:]  

def octal_para_binario(number):
    return bin(int(number, 8))[2:]

def convert_octal_to_decimal(number):
    return int(number, 8)

#-------------------binary-----------------------
def convert_decimal_to_binary(number):
    return bin(number)

def convert_binary_to_hexadecimal(number):
    return hex(int(number, 2))[2:]
        
def convert_binary_to_octal(number):
    return oct(int(number, 2))[2:] 

def convert_binary_to_decimal(number):
    return int(number, 2)

#------------------------conversão------------------------------

def conversion_numbers_to_decimal(number, 
                                  type_number):
    if type_number == "binary":
        number_conversion = convert_binary_to_decimal(number)
        return number_conversion
    
    elif type_number == "hexadecimal":
        number_conversion = convert_hexadecimal_to_decimal(number)
        return number_conversion
    
    elif type_number == "octal":
        number_conversion = convert_octal_to_decimal(number)
        return number_conversion
    
#-------------------------decimal para outros numeros----------------------------------------

def conversion_decimal_to_others_types(number, 
                                         type_number):
    
    if type_number == vars.options_our_convert[2]:
        binary = convert_decimal_to_binary(int(number))
        print(f"your decimal number is {number} and your decimal number converted a binary is {binary}")
    
    elif type_number == vars.options_our_convert[1]:
        hexadecimal = convert_decimal_to_hexadecimal(int(number))
        print(f"your decimal number is {number} and your decimal number converted a hexadecimal is {hexadecimal}")
    
    elif type_number == vars.options_our_convert[0]:
        octal = convert_decimal_to_octal(int(number))
        print(f"your decimal number is {number} and your decimal number converted a octal is {octal}")

    else:
        print("you didn't put any valid option, returning to the home menu")


def break_operation(start_operation):
    continue_operator = int(input("do you want to continue? Press 1 for yes or press 2 for no "))

    if continue_operator == 1:
        start_operation = True
        print("let's go again")
        return start_operation

    elif continue_operator == 2:
        start_operation = False
        print("see ya!")
        return start_operation
    

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
        
