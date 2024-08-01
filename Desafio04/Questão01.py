'''Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos'''

def soma_tres_argumentos(a, b, c):
    """
    Função que recebe três argumentos e retorna a soma deles.
    """
    return a + b + c

# Solicita ao usuário os três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chama a função e exibe o resultado
resultado = soma_tres_argumentos(numero1, numero2, numero3)
print(f"A soma dos três números é: {resultado}")