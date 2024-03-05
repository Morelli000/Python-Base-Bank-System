menu = """
###### DIO BANK ######

Selecione a opção desejada:

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair

=> """

LIMITE_SAQUES = 3
valor_maximo_saque = 500
saldo = 5000
i = 1
opcao = ""
extrato = []

while True:

    menu

    opcao = str(input(menu))

    if opcao == "1": # Depósito
        print("Opção Selecionada: Depósito")
        deposito = float(input("Valor para depósito: R$ "))

        if deposito > 0:

            saldo += deposito
            extrato.append("Depósito de R$ " + f"{deposito:.2f}")
            print(f"""Depósito realizado com sucesso. Saldo atual: R$ {saldo:.2f}""")
            retornar_ao_menu = str(input(f"Deseja voltar ao menu principal? \nS/N \n"))
            
            if retornar_ao_menu == "N":
                print("Obrigado por utilizar nosso Banco!")
                break

        else:
            print("Valor inválido. Retornando ao Menu Principal.")          
                

    elif opcao == "2": # Saque
        saque = float(input("Valor para saque: R$ "))
        
        if saque >= valor_maximo_saque:
            print("Valor superior ao limite de saque por operação. Retornando ao Menu Principal.")

        elif 0 < saque <= saldo and i <= LIMITE_SAQUES:
            i += 1
            saldo -= saque
            extrato.append("Saque de R$ " + f"{saque:.2f}")
            print(f"""Saque realizado com sucesso. Saldo atual: R$ {saldo:.2f}""")
            retornar_ao_menu = str(input(f"Deseja voltar ao menu principal? \nS/N \n"))
            
            if retornar_ao_menu == "N":
                print("Obrigado por utilizar nosso Banco!")
                break
        
        elif saque > saldo:
            print("Saldo insuficiente.")
        
        elif i > 3:
            print("Quantidade de saques diárias excedida. Entre em contato com seu gerente.")
            retornar_ao_menu = str(input(f"Deseja voltar ao menu principal? \nS/N \n"))
            
            if retornar_ao_menu == "N":
                print("Obrigado por utilizar nosso Banco!")
                break

        else:
            print("Valor inválido. Retornando ao menu principal")

    elif opcao == "3": # Extrato
        print("\n========== EXTRATO ==========\n")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(*extrato, sep="\n")
            print(f"Saldo atual: R$ {saldo:.2f}")
        print("\n=============================")

    elif opcao == "4":
        print("Obrigado por utilizar nosso Banco!")
        break