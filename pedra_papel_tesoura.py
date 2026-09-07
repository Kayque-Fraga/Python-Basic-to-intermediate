#Faça um programa que jogue pedra, papel, tesoura pelo teclado e mostre na tela o sua escolha\
#, do computador e mostre o resultado final.
import random

opcoes = ['pedra', 'papel', 'tesoura']
computador = random.choice(opcoes)
jogador = input('Pedra, papel ou tesoura? ').lower()

if jogador not in opcoes:
    print('Jogada incorreta!')

elif jogador == computador:
    print('Resultado: Empate! Escolha do jogador: {} e escolha do computador: {}'.format(jogador, computador))

elif (jogador == 'pedra' and computador == 'tesoura') or \
      (jogador == 'papel' and computador == 'pedra') or \
       (jogador == 'tesoura' and computador == 'papel'):
    print('Resultado: Vitória do jogador! Escolha do jogador: {} e escolha do computador: {}'.format(jogador, computador))

else:
    print('Resultado: Vitória do computador! Escolha do jogador: {} e escolha do computador: {}'.format(jogador, computador))
