'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.'''

numero = -1

while numero < 0 or numero > 10:
    numero = int(input('Digite sua nota, sendo entre zero e dez:'))
    if numero < 0 or numero > 10:
        print('Número inválido, tente novamente!')

print('Número válido inserido com sucesso!')