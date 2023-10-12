# ATM

def atm():
    cem = 0
    cinquenta = 0
    vinte = 0
    dez = 0
    cinco = 0
    cash = 0

    saque = int(input("Este ATM é abastecido com notas de 5, 10, 20, 50 e 100 reias. Quanto você deseja sacar? R$"))
    print(saque)
    total = saque

    cem = saque / 100
    saque = saque - int(cem) * 100
    cinquenta = saque / 50
    saque = saque - int(cinquenta) * 50
    vinte = saque / 20
    saque = saque - int(vinte) * 20
    dez = saque / 10
    saque = saque - int(dez) * 10
    cinco = saque / 5

    print('Notas R$ 100,00 = ',int(cem))
    print('Notas R$  50,00 = ',int(cinquenta))
    print('Notas R$  20,00 = ',int(vinte))
    print('Notas R$  10,00 = ',int(dez))
    print('Notas R$   5,00 = ',int(cinco))
