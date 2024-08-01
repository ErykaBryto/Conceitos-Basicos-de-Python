'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

contagem_pares = 0
contagem_impares = 0

while True:
    numero = int(input("Digite um número positivo (ou 0 para encerrar): "))
    
    if numero == 0:
        break

    if numero < 0:
        print("Número inválido. Apenas números positivos são permitidos.")
        continue

    if numero % 2 == 0:
        contagem_pares += 1
    else:
        contagem_impares += 1

print(f"Quantidade de números pares: {contagem_pares}")
print(f"Quantidade de números ímpares: {contagem_impares}")