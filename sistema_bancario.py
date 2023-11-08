menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

       excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor > saldo:
            print("Sem saldo suficiente para realizar o saque.")

        elif valor > limite:
            print("O valor do saque é maior que o limite permitido por operação.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "e":
        print("\nEXTRATO")
        print(f"{extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
