while True:

  numero_hexa = ""
  binario = ""
  decimal = 0
  octal = ""
  hexadecimal = ""

  i = 0
  caracteres_hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
  resto = []
  

  print("\nInforme o Tipo do Numero\n", "1 - Binario\n", "2 - Octal\n",
        "3 - Decimal\n", "4 - Hexadecimal")
  tipo = int(input("Digite o Numero da Opção: "))

  if tipo == 1:
    numero = input("\nDigite o Numero Binario: ")
    for i in range(len(numero)):
      decimal += int(numero[i]) * 2**(len(numero) - 1 - i)
    print("\nO Numero Decimal é: ", decimal)

    continuar = input("Deseja Continuar (s/n): ")
    if continuar == "n":
      break

  elif tipo == 2:
    numero = input("\nDigite o Numero Octal: ")
    for i in range(len(numero)):
      decimal += int(numero[i]) * 8**(len(numero) - 1 - i)

    print("\nO Numero Decimal é: ", decimal)
    continuar = input("Deseja Continuar (s/n): ")
    if continuar == "n":
      break

  elif tipo == 3:
    print("\nInforme o Tipo do Numero\n", "1 - Binario\n", "2 - Octal\n","3 - Hexadecimal")
    tipo2 = int(input("Digite o Numero da Opção: "))
    if tipo2 == 1:
      numero = int(input("\nDigite o Numero Decimal: "))
      while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
      print("\nO Numero Binario é: ", binario)
      continuar = input("Deseja Continuar (s/n): ")
      if continuar == "n":
        break
    elif tipo2 == 2:
      numero = int(input("\nDigite o Numero Decimal: "))
      while numero > 0:
        resto = numero % 8
        octal = str(resto) + octal
        numero = numero // 8
      print("\nO Numero Octal é: ", octal)
      continuar = input("Deseja Continuar (s/n): ")
      if continuar == "n":
        break
    elif tipo2 == 3:
      numero = int(input("\nDigite o Numero Decimal: "))
      #converte decimal para hexadecimal e caso o valor for 1010 aparece AA
      while numero > 0:
        resto.append(caracteres_hex[(numero % 16)])
        n = numero // 16
      for i in range(len(resto)-1,-1,-1):
        print(resto[i],end="")
      
      continuar = input("Deseja Continuar (s/n): ")
      if continuar == "n":
        break
    else:
      print("Opção Invalida")
  elif tipo == 4:
    hexadecimal = input("Digite um número hexadecimal: ").upper()
    decimal = 0

    for i in range(len(hexadecimal)):
        digit = hexadecimal[len(hexadecimal) - 1 - i]
        if digit.isdigit():
            decimal += int(digit) * (16 ** i)
        else:
            decimal += (ord(digit) - 55) * (16 ** i)

    print("O número decimal equivalente é:", decimal)
    
    continuar = input("Deseja Continuar (s/n): ")

    if continuar == "n":
      break

  else:
    print("\nOpção invalida\n") 