'''def soma(): #definição da função soma
    calculo = 10+2
    print(f'O resultado da soma é:{calculo}')'''

'''def subtracao():
    sub = 10-2
    print(f'O resultado da subtração é:{sub}')
    multiplicacao() # chamada de função dentro de uma função
'''
'''def multiplicacao():
    mult = 10*2
    print(f'O resultado da multiplicação é:{mult}')
'''

#chamada da função
'''soma()
subtracao()'''

'''def soma():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    calculo = num1+num2
    print(f'O resultado da soma é:{calculo}')'''

# Parametros para deixar o codigo mais flexível
def soma(num1, num2):
    calculo = num1+num2
    print(f'O resultado da soma é:{calculo}')

def subtracao(num1, num2):
    sub = num1-num2
    print(f'O resultado da subtração é:{sub}')
    

def multiplicacao(num1, num2):
    mult = num1*num2
    print(f'O resultado da multiplicação é:{mult}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
#chamada da função
soma(num1,num2)
subtracao(num1,num2)
multiplicacao(num1, num2)
