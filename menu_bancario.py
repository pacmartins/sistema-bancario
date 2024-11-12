import textwrap

def menu():
    menu = """\n
    \t\t\t\tMENU
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q] Sair
    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    pass

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass

def extrato(saldo, /, *, extrato):
    pass

def incluir_usuario(usuarios):
    pass

def filtrar_usuario(cpf, usuarios):
    pass

def criar_conta(agencia, numero_conta, usuarios):
    pass

def listar_contas(contas):
    pass


def antigo():
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

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informa o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
            #print("Selecionando opção de SACAR.")

        elif opcao == "e":
            extrato(saldo, extrato=extrato)
            #print("Selecionando opção de EXTRATO.")

        elif opcao == "nu":
            usuarios(usuarios)
            #print("Selecionando opção de inclusão de NOVO USUÁRIO.")

        elif opcao == "nc":
            numero_contas = len(contas) + 1
            print("Selecionando opção de inclusão de NOVA CONTA.")
        elif opcao == "lc":
            print("Selecionando opção de LISTAR CONTAS.")
        elif opcao == "q":
            print("\nVocê está saindo do sistema bancário!\nObrigado por usar o nosso programa!")
            break
        else:
            print("Operação inválida!\nPor favor, selecione novamente a operação desejada\n ou selecione 'q' para SAIR.")

main()