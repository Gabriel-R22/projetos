cores = (
    '\033[m', # fechar cor
    '\033[1;31m', # cor de fundo vermelha
)


def mensagem():
    msg = 'MENU PRINCIPAL'
    qnt = len(msg) + 16
    print('~'*qnt)
    print(msg.center(qnt))
    print('~'*qnt)
    print('\033[1;33m1\033[m - \033[1;34mVer pessoas cadastradas\033[m')
    print('\033[1;33m2\033[m - \033[1;34mCadastrar nova pessoa\033[m')
    print('\033[1;33m3\033[m - \033[1;34mSair do sistema\033[m')



def lista():
    msg = 'PESSOAS CADASTRADAS'
    qnt = len(msg) + 15
    print('~'*qnt)
    print(msg.center(qnt))
    print('~'*qnt)


def cadastro():
    msg = 'NOVO CADASTRO'
    qnt = len(msg) + 10
    print('~'*qnt)
    print(msg.center(qnt))
    print('~'*qnt)


def saida():
    print(cores[1])
    msg = 'Saindo do sistema... ATÉ LOGO!'
    qnt = len(msg) + 10
    print('~'*qnt)
    print(msg.center(qnt))
    print('~'*qnt)
    print(cores[0])
