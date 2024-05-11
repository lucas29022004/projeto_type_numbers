import defs, vars

def main():
    defs.clear_terminal()
    start_operation = True
    while start_operation:

        print("+------------------+")
        print("|   options        |")
        print("+------------------+")
        print("|   octal          |")
        print("|   hexadecimal    |")
        print("|   binary         |")
        print("|   decimal        |")
        print("+------------------+ \n")

        conversion_first_number = input("what option you will using (write the option): ").lower()
        first_number = input("enter the number equivalent to the chosen option: ")

        if conversion_first_number == vars.options_our_convert[0]:
            decimal = defs.convert_octal_to_decimal(first_number)
            print(f"your number octal is {first_number} and your octal number converted a decimal is {decimal}")
            start_operation = defs.break_operation(start_operation)

        elif conversion_first_number == vars.options_our_convert[1]:
            decimal = defs.convert_hexadecimal_to_decimal(first_number)
            print(f"your number hexadecimal is {first_number} and your hexadecimal number converted a decimal is {decimal}")
            start_operation = defs.break_operation(start_operation)

        elif conversion_first_number == vars.options_our_convert[2]:
            decimal = defs.convert_binary_to_decimal(first_number)
            print(f"your number binary is {first_number} and your binary number converted a decimal is {decimal}")
            start_operation = defs.break_operation(start_operation)

        elif conversion_first_number == vars.options_our_convert[3]:
            print("what type of conversion do you need for your decimal number")
            print("+------------------+")
            print("|   options        |")
            print("+------------------+")
            print("|   octal          |")
            print("|   hexadecimal    |")
            print("|   binary         |")
            print("+------------------+ \n")

            conversion_second_number = input("what option you will using to conversion your decimal number (write the option): ").lower()
            # second_number = input("enter the number equivalent to the chosen option: ")

            defs.conversion_decimal_to_others_types(number = first_number,
                                                    type_number = conversion_second_number)
            start_operation = defs.break_operation(start_operation)
            
        else:
            print("\nyou didn't put any valid option, returning to the home menu")
            start_operation = defs.break_operation(start_operation)

main()    
