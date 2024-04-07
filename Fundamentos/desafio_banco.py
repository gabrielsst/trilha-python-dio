menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        while True:
            while True:
                try:
                    valor = float(input("\nInforme o valor do depósito: "))
                    break
                except:
                    print("\nOperação falhou! Digite um número.")
                    continue
            
            if valor > 0:
                saldo += valor
                extrato += f"\nDepósito: R$ {valor:.2f}"
                break
            else:
                print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "s":
        while True:
            while True:
                    try:
                        valor = float(input("\nInforme o valor do depósito: "))
                        break
                    except:
                        print("\nOperação falhou! Digite um número.")
                        continue

            if valor > saldo:
                print("\nOperação falhou! Você não tem saldo suficiente.")
                break

            elif valor > LIMITE:
                print("\nOperação falhou! O valor do saque excede o limite.")
                break

            elif numero_saques >= LIMITE_SAQUES:
                print("\nOperação falhou! Número máximo de saques excedido.")
                break

            elif valor > 0:
                saldo -= valor
                extrato += f"\nSaque: R$ {valor:.2f}"
                numero_saques += 1
                break

            else:
                print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")