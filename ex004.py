#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo\
#e todas as informações possiveis sobre ele.

teclado = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(teclado))
print('Só tem espaços?', teclado.isspace())
print('É um número?', teclado.isnumeric())
print('É alfabético?', teclado.isalpha())
print('É alfanumérico?', teclado.isalnum())
print('Está em maiúsculas?', teclado.isupper())
print('Está em minúsculas?', teclado.islower())
print('Está capitalizada?', teclado.istitle())
