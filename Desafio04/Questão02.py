'''Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

def reverso_numero(numero):
    """
    Função que retorna o reverso de um número inteiro.
    """
    # Converte o número para uma string, inverte a string e converte de volta para inteiro
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chama a função e exibe o resultado
resultado = reverso_numero(numero)
print(f"O reverso do número {numero} é: {resultado}")
