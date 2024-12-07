continuar = "S"
i = 2
while continuar == "S":
    numero = float(input("Digite um número: \n"))
    if numero < i:
        print("Seu número não é primo. ")
    elif numero % i == 0:
        print("Seu número não é primo. ")
    else:
        print("Seu número é primo.")

    continuar = str(input('Deseja continuar? (S/N)'))
    if continuar != 'S':
        break

print("Fim.")