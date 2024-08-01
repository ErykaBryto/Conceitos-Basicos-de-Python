'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Ordenar os números em ordem crescente
if numero1 <= numero2 <= numero3:
    # Caso 1: numero1 é o menor, numero2 é o intermediário e numero3 é o maior
    print(f"Ordem crescente: {numero1}, {numero2}, {numero3}")
elif numero1 <= numero3 <= numero2:
    # Caso 2: numero1 é o menor, numero3 é o intermediário e numero2 é o maior
    print(f"Ordem crescente: {numero1}, {numero3}, {numero2}")
elif numero2 <= numero1 <= numero3:
    # Caso 3: numero2 é o menor, numero1 é o intermediário e numero3 é o maior
    print(f"Ordem crescente: {numero2}, {numero1}, {numero3}")
elif numero2 <= numero3 <= numero1:
    # Caso 4: numero2 é o menor, numero3 é o intermediário e numero1 é o maior
    print(f"Ordem crescente: {numero2}, {numero3}, {numero1}")
elif numero3 <= numero1 <= numero2:
    # Caso 5: numero3 é o menor, numero1 é o intermediário e numero2 é o maior
    print(f"Ordem crescente: {numero3}, {numero1}, {numero2}")
else:
    # Caso 6: numero3 é o menor, numero2 é o intermediário e numero1 é o maior
    print(f"Ordem crescente: {numero3}, {numero2}, {numero1}")