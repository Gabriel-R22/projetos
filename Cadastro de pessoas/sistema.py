import functions as msg
from time import sleep

while True:
    msg.mensagem()
    print('~'*30)
    sleep(0.2)
    opção = int(input('\033[1;33mSua opção: \033[m'))
    if opção == 1:
        msg.lista()
        cadastro = open('pessoas.txt', 'r')
        for p in cadastro.readlines():
            p = p.rstrip('\n')
            print(p)
            sleep(0.5)
        print('~'*35)
        sleep(2)
    elif opção == 2:
        msg.cadastro()
        pessoa = str(input('\033[1;33mDigite o nome da pessoa: \033[m'))
        idade = int(input('\033[1;33mDigite a idade: \033[m'))
        try:
            cadastro = open('pessoas.txt', 'a')
            cadastro.write(f'{pessoa:<18}   {idade} anos\n')
        finally:
            cadastro.close()
        sleep(0.5)
    elif opção == 3:
        msg.saida()
        sleep(0.2)
        break
