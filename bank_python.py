menu = " "

#[d] Deposito
#[s] Saque
#[e] Extrato
#[q] Sair


saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3
#format(saldo, ",.2f")
while True:
    opcao = input(menu)
    
    if opcao == "d" :
        valor = int(input('Digite o valor de deposito: '))
        if valor < 0 :
            print('Valor INVALIDO!')
        else:
            saldo = valor
            print(format(valor, ",.2f") 'foram depositados na sua conta')
            
    elif opcao == "s":
        saque = int(input('Digite o valor de saque: '))
        if saque > 500:
            print('Você excedeu o valor de saque, limite: 500')
        elif saque > saldo:
            print('Saque INVALIDO! seu saldo é de: 'format(saldo, ",.2f") )
        else: 
            saldo = saldo - saque 
            print('Operação concluida com SUCESSO')
            
    elif opcao == "e":
        print("\n ============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: r$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")