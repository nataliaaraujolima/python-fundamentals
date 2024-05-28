num1 = 0
num2 = 0

num1 = int(input("Insira o numero A:: \n"))
num2 = int(input("Insira o numero B:: \n"))

soma = num1 + num2

if soma >= 10:
    print(f"{soma} é > ou = 10")
else:
    print(f"{soma} NAO é > ou = 10")
