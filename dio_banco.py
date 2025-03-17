def menu():
    return """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """


def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro! O valor do depósito deve ser positivo.")
    except ValueError:
        print("Erro! Digite um valor numérico válido.")
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Erro! O valor do saque deve ser positivo.")
        elif valor > saldo:
            print("Erro! Saldo insuficiente.")
        elif valor > limite:
            print(f"Erro! O limite de saque é R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Erro! Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    except ValueError:
        print("Erro! Digite um valor numérico válido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("\n".join(extrato) if extrato else "Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu()).strip().lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema! Até logo.")
            break
        else:
            print("Opção inválida! Escolha uma das opções do menu.")


if __name__ == "__main__":
    main()
