'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''


saudacao= input("Informe o turno que você estuda, Sendo M para matutino, V para Vespertino e N para Noturno!")

if saudacao == 'M' or saudacao == 'm':
    print('Bom dia!')
elif saudacao == 'V' or saudacao == 'v':
    print('Boa tarde!')
elif saudacao == 'N' or saudacao == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido!')