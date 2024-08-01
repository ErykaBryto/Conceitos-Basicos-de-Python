'''Faça um Programa que peça dois números e imprima o maior deles.'''

numero01 = float(input('Digite o primeiro número: '))
numero02 = float(input('Digite o segundo número: '))

if numero01 > numero02:
    print(f"O número {numero01:.2f} é o maior!")
else:
    print(f"O número {numero02:.2f} é o maior!")