from time import sleep

codigo = ()
produto = ()
preço = ()

while True:
    print('-='*10)
    print(f'{"MENU":^20}')
    print('-='*10)
    opções = int(input('[ 1 ] Cadastro\n[ 2 ] Caixa\n--> '))
    while True:
        if opções == 1:
            print('-'*10)
            print(f'{"CADASTRO":^10}')
            print('-'*10)
            code = input('Digite o código do produto: ')
            codigo += (code,)
            pdt = input('Digite o nome do produto: ')
            produto += (pdt,)
            valor = float(input('Digite o valor do produto: R$'))
            preço += (valor,)
            continuar1 = input('Quer continuar a cadastrar? [S/N] ').upper().strip()[0]
            if continuar1 == 'N':
                break
            while continuar1 not in 'SN':
                continuar1 = input('Quer continuar a cadastrar? [S/N] ').upper().strip()[0]
        if opções == 2:
            break
    print('-='*10)
    print(f'{"CAIXA":^20}')
    print('-='*10)
    pdt2 = ()
    valor2 = ()
    while True:
        code2 = input('Digite o código do produto: ')
        while code2 not in codigo:
            code2 = input('Digite o código do produto: ')
        pos = codigo.index(code2)
        pdt2 += (produto[pos], )
        valor2 += (preço[pos], )
        continuar2 = input('Quer continuar a compra? [S/N] ').upper().strip()[0]
        if continuar2 == 'N':
            break
        while continuar2 not in 'SN':
            continuar2 = input('Quer continuar a compra? [S/N] ').upper().strip()[0]
    total = 0
    print('-'*35)
    print(f'{"COMPRA FINAL":^35}')
    print('-'*35)
    for preço2 in valor2:
        total += preço2
    for cont in range(0, len(pdt2)):
        print(f'{pdt2[cont]:.<20}', end=' ')
        print(f'R${valor2[cont]:>.2f}')
    print(f'\nTOTAL: R${total:.2f}')
    print('-'*35)
    dinheiro = float(input('Digite o dinheiro recebido: R$'))
    troco = dinheiro - total
    if troco == 0:
        print('Não é necessário troco!')
    while dinheiro < total:
        print('Dinheiro insuficiente!')
    else:
        print(f'Troco: R${troco:.2f}')
    pdt2 = ()
    valor2 = ()
    sleep(3)