import vars
import pandas as pd

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

def conversion_decimal_to_others_numbers(number, 
                                         type_number):
    if type_number == "binary":
        number_conversion = convert_decimal_to_binary(number)
        return number_conversion
    
    elif type_number == "hexadecimal":
        number_conversion = convert_decimal_to_hexadecimal(number)
        return number_conversion
    
    elif type_number == "octal":
        number_conversion = convert_decimal_to_octal(number)
        return number_conversion
    



def conversion_decimal_to_other_types(number, 
                                      type_number):

    for option in vars.options_our_convert:
        if type_number == option:
            conversion_number = conversion_decimal_to_others_numbers(number,
                                                                  type_number)
            return conversion_number



#----------calculator---------------------------

def calculator(converted_first_number_to_decimal,
               converted_second_number_to_decimal,
               conversion_first_number,
               conversion_second_number,
               real_first_number,
               real_second_number
               ):
    
        print("+-------------+---------------+")
        print("|   options   | description   |")
        print("+-------------+---------------+")
        print("|   +         | Addition      |")
        print("|   -         | Subtraction   |" )
        print("|   *         | Multiplication|" )
        print("|   /         | Divison       |")
        print("+-------------+---------------+ \n")


        operator = input('which operator our use: ')
        if operator == "+":
            addition_result = converted_first_number_to_decimal + converted_second_number_to_decimal

            print(f"converted_first_number_to_decimal: {converted_first_number_to_decimal}")
            converted_first_number = conversion_decimal_to_other_types(converted_first_number_to_decimal,
                                                                       conversion_first_number)
            
            converted_second_number = conversion_decimal_to_other_types(converted_second_number_to_decimal,
                                                                        conversion_second_number)
            
            print(f"converted_first_number: {converted_first_number}")

            data = {"first number you entered": [f"{real_first_number}"],
                    "second number your entered": [f"{real_second_number}"],
                    "first_number_converted": [f"{converted_first_number}"],
                    "second_number_converted": [f"{converted_second_number}"],
                    "result_of_operation": [f"{addition_result}"]}
            
            df = pd.DataFrame(data)
            print(df)
            


  


            




            






# def validation_number(self, number):
#     if number.isdigit():
#         return "Decimal"
#     elif all(digit in "01" for digit in number):
#         return "Binário"
#     elif all(digit in "0123456789" for digit in number):
#         return "Decimal"
#     elif all(digit in "0123456789abcdefABCDEF" for digit in number):
#         return "Hexadecimal"
#     elif all(digit in "01234567" for digit in number):
#         return "Octal"
#     else:
#         raise "o numero que você colocou não satisfaz nenhuma dessas categorias: \n".join(self.options_our_convert)
    
    