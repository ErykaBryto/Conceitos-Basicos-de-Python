'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.'''

# Lista para armazenar as médias dos alunos
medias = []

# Loop para pedir as notas de 5 alunos
for i in range(5):
    print(f"\nDigite as notas do aluno {i + 1}:")
    
    # Lista para armazenar as quatro notas de um aluno
    notas = []
    
    # Loop para pedir as quatro notas de um aluno
    for j in range(4):
        nota = float(input(f"Nota {j + 1}: "))
        notas.append(nota)
    
    # Calcula a média das notas do aluno e armazena na lista de médias
    media = sum(notas) / 4
    medias.append(media)

# Conta o número de alunos com média maior ou igual a 7.0
alunos_acima_7 = len([media for media in medias if media >= 7.0])

# Imprime o número de alunos com média maior ou igual a 7.0
print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima_7}")
