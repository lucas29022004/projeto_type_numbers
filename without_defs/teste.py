hexadecimal = input("Digite um número hexadecimal: ").upper()
decimal = 0

for i in range(len(hexadecimal)):
    digit = hexadecimal[len(hexadecimal) - 1 - i]
    if digit.isdigit():
        decimal += int(digit) * (16 ** i)
    else:
        decimal += (ord(digit) - 55) * (16 ** i)

print("O número decimal equivalente é:", decimal)