'''Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''

def calcular_moedas(dinheiro):
    """
    Calcula quanto a pessoa pode comprar de cada moeda estrangeira com o dinheiro disponível.
    """
    # Taxas de conversão
    conversao = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suiço': 0.42,
        'Euro': 5.36,
        'Libra Esterlina': 6.21
    }

    # Calcula a quantidade de cada moeda que pode ser comprada
    resultado = {}
    for moeda, taxa in conversao.items():
        quantidade = dinheiro / taxa
        resultado[moeda] = quantidade
    
    return resultado

# Solicita ao usuário o valor em reais
dinheiro = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))

# Calcula quanto pode ser comprado de cada moeda
moedas = calcular_moedas(dinheiro)

# Exibe o resultado
print("\nCom R$ {:.2f}, você pode comprar:" .format(dinheiro))
for moeda, quantidade in moedas.items():
    print(f"{quantidade:.2f} de {moeda}")
