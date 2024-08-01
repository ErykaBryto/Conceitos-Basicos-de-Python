'''Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.'''

def contar_vogais(frase):
    """
    Conta o número de vogais em uma string.
    """
    # Definição das vogais
    vogais = 'aeiouAEIOU'
    
    # Inicializa o contador de vogais
    contador = 0
    
    # Conta as vogais na string
    for caractere in frase:
        if caractere in vogais:
            contador += 1
    
    return contador

# Solicita ao usuário que insira uma frase
frase_usuario = input("Digite uma frase: ")

# Conta as vogais na frase fornecida pelo usuário
total_vogais = contar_vogais(frase_usuario)

# Exibe o resultado
print(f"A frase fornecida contém {total_vogais} vogais.")
