from time import sleep

cores = (
    '\033[m', # fechar cor
    '\033[7;30;41m', # cor de fundo vermelha
    '\033[7;30;44m', # cor de fundo azul
    '\033[7;30;42m', # cor de fundo branca
    '\033[7;30;43m', # cor de fundo roxa
)

def pyhelp(ajuda, color=0):
    """
    -> Função que retorna o help de um comando ou a mensagem de saída
    """
    print(cores[color])
    help(ajuda)
    print(cores[0])


def mensagem(msg, color=0):
    """
    -> Função para imprimir o nome do sistema (PyHELP)
    """
    qnt = len(msg) + 4
    print(cores[color])
    print('~'*qnt)
    print(f'{msg:^{qnt}}')
    print('~'*qnt)
    print(cores[0])


# Programa principal
while True:
    mensagem('SISTEMA DE AJUDA PyHELP', 4)
    sleep(0.5)
    comando = input('Digite uma função ou biblioteca > ').lower()
    sleep(1)
    if comando == 'fim':
        mensagem('ATÉ LOGO!', 1)
        break
    else:
        mensagem(f'Acessando as informações do comando {comando}', 3)
        sleep(0.5)
        pyhelp(comando, 2)
        sleep(2)