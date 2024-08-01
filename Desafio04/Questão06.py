'''Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício'''

import random

def escolher_palavra():
    """
    Escolhe uma palavra secreta aleatoriamente de uma lista predefinida.
    """
    palavras = ['python', 'programacao', 'desenvolvimento', 'jogo', 'computador']
    return random.choice(palavras)

def exibir_palavra(palavra_secreta, letras_corretas):
    """
    Exibe a palavra secreta com as letras adivinhadas e espaços em branco para letras não adivinhadas.
    """
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra_secreta])

def jogo_forca():
    """
    Função principal do jogo de forca.
    """
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    tentativas = 6
    letras_erradas = set()
    
    print("Bem-vindo ao jogo da forca!")
    
    while tentativas > 0:
        print("\n" + exibir_palavra(palavra_secreta, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if letra in palavra_secreta:
            letras_corretas.add(letra)
            if set(palavra_secreta) <= letras_corretas:
                print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print(f"Letra errada! Você tem {tentativas} tentativas restantes.")
    
    if tentativas == 0:
        print(f"Você perdeu! A palavra secreta era: {palavra_secreta}")

# Inicia o jogo
jogo_forca()
