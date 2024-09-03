comandos = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
print(comandos)
saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while  True:
    entrada = input("Digite a operação que deseja")
    if entrada == "s":
        if LIMITE_SAQUES > numero_saques:
            
            if saldo > 0:
                sacar = int(input("valor para sacar : "))
                if sacar <= LIMITE:
                    resultado = saldo - sacar
                    print(f'valor sacado : {sacar}')
                    extrato += f'Saque : R$ {sacar}'
                    numero_saques +=1
                elif sacar > LIMITE:
                    print("ultrapassou o limite de saque")

        elif LIMITE_SAQUES < numero_saques:
            print("voçê ultrapassou o limite de saque")
            break

    elif entrada == "d":
        depositar = int(input("Digite o valor para deposito : "))
        if depositar > 0:
            saldo += depositar
            print(f"Seu saldo atual {saldo}")
            extrato += f'Deposito : R$ {depositar}'

        elif depositar < 0:
            print("Esse valor não pode ser depositado")

    elif entrada == "q":
        print("volte sempre")
        break
    
    elif entrada == "e":
        if not extrato:
            print("********extrato********")
            print("***********sem movimentaçôes************")

        else:
            extrato
            print("\n*********extrato********")
            print("\n*****suas movimentaçôes*******")
            print(f"\n***** {extrato}")
    else:
        print("operação nâo identificada, tente novamente")
    
