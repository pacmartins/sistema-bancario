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
            print("Operação inválida!\nO valor informado não pode ser 0 (zero) ou negativo.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação inválida!\nVocê não tem saldo suficiente.")
        elif valor > limite:
            print("Operação inválida!\nO valor do saque excede o limite.")
        elif valor > 0:
            if numero_saques >= LIMITE_SAQUES:
                print("Operação inválida!\nNúmero máximo de saques excedido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e":
        print("\n                 EXTRATO                 ")
        print("\n=========================================")

        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida!\nPor favor, selecione novamente a operação desejada.")