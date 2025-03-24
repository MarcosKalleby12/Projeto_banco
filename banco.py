menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def depositar(value):
    global saldo
    global extrato
    print(f'Você depositou R$ {value:.2f}') 
    saldo += value
    extrato += f'Depositado R$ {value:.2f}\n'

def sacar(value):
    global saldo
    global extrato
    global numero_saques 
    numero_saques += 1
    print(f'Você ultilizou {numero_saques}/3 saques disponíveis')
    print(f'Você sacou R$ {value:.2f}')
    saldo -= value
    extrato += f'Sacado R$ {value:.2f}\n'

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    input_user = input(menu)

    if input_user.isdigit():
        print('Erro, a informação digitada é um número')
        continue
    
    if input_user == 'd':
        try:
            deposit_input = input('Digite um valor para depositar: ')
            float_deposit = float(deposit_input)
        except ValueError:
            print('Erro, valor inválido')
            continue
        
        if float_deposit < 0:
            print('Erro, valor inválido')
            continue
        depositar(float_deposit)
        continue
    
    elif input_user == 's':
        if numero_saques == 3:
            print('Erro, qtd. máxima de saques atingido')
            continue

        print(f'O limite do valor de saque é de R$ {limite}')
        try:
            cashout_input = input('Digite um valor para sacar: ')
            float_cashout = float(cashout_input)
        except ValueError:
            print('Erro, valor inválido')
            continue

        if float_cashout < 0 or float_cashout > limite:
            print('Erro, valor inválido')
            continue
        elif saldo < float_cashout:
            print('Erro, saldo insuficiente')
            continue
        else:
            sacar(float_cashout)
            continue

    elif input_user == 'e':
        print(extrato)
        print(f'Total: R$ {saldo}')
        continue
    
    elif input_user == 'q':
        print('Saindo do sistema')
        break

    else:
        print('Erro, opção inválida')

        


    