def preço(larg, comp, val):
    area = larg * comp
    preçoPm = val / area
    print(f'O valor por m² de um terreno de {area:.2f}m² ({larg}x{comp}) é de R${preçoPm:.2f}')  


def mensagem():
    print('-'*35)
    print(f'{"CALCULADORA DE VALOR DO M²":^35}')
    print('-'*35)


mensagem()
valor = float(input('Digite o valor do terreno: R$'))
largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento de um terreno (m): '))
preço(largura, comprimento, valor)