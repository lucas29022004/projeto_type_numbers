# hexadecimal = input("Digite um número hexadecimal: ").upper()
# decimal = 0

# for i in range(len(hexadecimal)):
#     digit = hexadecimal[len(hexadecimal) - 1 - i]
#     if digit.isdigit():
#         decimal += int(digit) * (16 ** i)
#     else:
#         decimal += (ord(digit) - 55) * (16 ** i)

# print("O número decimal equivalente é:", decimal)


decimal_number = int(input("Digite um número decimal: "))
hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

hexadecimal = ""
while decimal_number > 0:
    remainder = decimal_number % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = hex_map[remainder] + hexadecimal
    decimal_number //= 16

print("O número hexadecimal correspondente é:", hexadecimal)