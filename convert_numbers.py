import vars
import defs

 


        


def main():
    start_calculator = True
    while start_calculator == True:

        print("+------------------+")
        print("|   options        |")
        print("+------------------+")
        print("|   octal          |")
        print("|   hexadecimal    |")
        print("|   binary         |")
        print("|   decimal        |")
        print("|   no conversion  |")
        print("+------------------+ \n")

        what_is_a_conversion_first_number = input("when option you will using to conversion at first number: ").lower()
        what_is_a_conversion_second_number = input("when option you will using to conversion at first number: ").lower()

        if what_is_a_conversion_first_number and what_is_a_conversion_second_number in vars.options_our_convert:
        
            which_a_first_number = input("send me a number: ").lower()
            first_number_type = input("which of the options is this number: ")
            which_a_second_number = input("send me a number: ").lower()
            second_number_type = input("which of the options is this number: ")

            #---------------convertendo pra decimal para ser feito o calculo-----------
            first_number = defs.conversion_numbers_to_decimal(which_a_first_number, 
                                                              first_number_type)
            
            second_number = defs.conversion_numbers_to_decimal(which_a_second_number,
                                                               second_number_type)
            

            defs.calculator(first_number,
                            second_number,
                            what_is_a_conversion_first_number,
                            what_is_a_conversion_second_number,
                            which_a_first_number,
                            which_a_second_number
                            )


            break

        
            
        else:
            print(f"você colocou uma opção invalida, essas são as opões validas \n ".join(vars.options_our_convert))

        
        

    

main()    

            




        

        


    
        
       