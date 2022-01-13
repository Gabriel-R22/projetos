import random
import time

# contador do jogador
vitorias = 0
derrotas = 0
empates = 0

# contador da cpu
cpuVitorias = 0
cpuDerrotas = 0
cpuEmpates = 0

while True:
    print('-='*12)
    print(' PEDRA, PAPEL, TESOURA')
    print('-='*12)
    print('INICIANDO O JOGO...')
    time.sleep(2)

    jogador = str(input('Escolha entre Pedra, Papel e Tesoura\n--> ')).upper().strip()
    while jogador not in 'PEDRAPAPELTESOURA':
        jogador = str(input('Escolha entre Pedra, Papel e Tesoura\n--> ')).upper().strip()

    opções = ('Pedra', 'Papel', 'Tesoura')
    cpu = random.choice(opções)

    print('CALCULANDO RESULTADOS...')
    time.sleep(2)

    print(f'Você escolheu {jogador.capitalize()}')
    print(f'A CPU escolheu {cpu}')

    # possibilidades de empate
    if jogador == 'PEDRA' and cpu == 'Pedra':
        print('JOGO EMPATADO')
        empates += 1
        cpuEmpates += 1
    elif jogador == 'PAPEL' and cpu == 'Papel':
        print('JOGO EMPATADO')
        empates += 1
        cpuEmpates += 1
    elif jogador == 'TESOURA' and cpu == 'Tesoura':
        print('JOGO EMPTADO')
        empates += 1
        cpuEmpates += 1

    # possibilidades de vitória
    if jogador == 'PEDRA' and cpu == 'Tesoura':
        print('VOCÊ VENCEU!')
        vitorias += 1
        cpuDerrotas += 1
    elif jogador == 'PAPEL' and cpu == 'Pedra':
        print('VOCÊ VENCEU!')
        vitorias += 1
        cpuDerrotas += 1
    elif jogador == 'TESOURA' and cpu == 'Papel':
        print('VOCÊ VENCEU!')
        vitorias += 1
        cpuDerrotas += 1

    # possibilidades de derrota
    if jogador == 'PEDRA' and cpu == 'Papel':
        print('VOCÊ PERDEU!')
        derrotas += 1
        cpuVitorias += 1
    elif jogador == 'PAPEL' and cpu == 'Tesoura':
        print('VOCÊ PERDEU!')
        derrotas += 1
        cpuVitorias += 1
    elif jogador == 'TESOURA' and cpu == 'Pedra':
        print('VOCÊ PERDEU')
        derrotas += 1
        cpuVitorias += 1

    continuar = str(input('Quer jogar novamente? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer jogar novamente? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('Gerando o placar...')
time.sleep(2)

print('-'*10)
print('  PLACAR')
print('-'*10)
print('POSIÇÃO    V  D  E')
if vitorias > cpuVitorias:
    print(f'Jogador    {vitorias}  {derrotas}  {empates}\nCPU        {cpuVitorias}  {cpuDerrotas}  {cpuEmpates}')
    print('YOU ARE THE WORLD CHAMPION!')
elif cpuVitorias > vitorias:
    print(f'CPU        {cpuVitorias}  {cpuDerrotas}  {cpuEmpates}\nJogador    {vitorias}  {derrotas}  {empates}')
    print('GAME OVER')
elif vitorias == cpuVitorias and cpuDerrotas > derrotas:
    print(f'Jogador    {vitorias}  {derrotas}  {empates}\nCPU       {cpuVitorias}  {cpuDerrotas}  {cpuEmpates}')
    print('YOU ARE THE WORLD CHAMPION!')
elif vitorias == cpuVitorias and cpuDerrotas < derrotas:
    print(f'CPU        {cpuVitorias}  {cpuDerrotas}  {cpuEmpates}\nJogador    {vitorias}  {derrotas}  {empates}')
    print('GAME OVER')
elif vitorias == cpuVitorias and derrotas == cpuDerrotas:
    print(f'Jogador    {vitorias}  {derrotas}  {empates}\nCPU        {cpuVitorias}  {cpuDerrotas}  {cpuEmpates}')
    print('NINGUÉM VENCEU O CAMPEONATO')