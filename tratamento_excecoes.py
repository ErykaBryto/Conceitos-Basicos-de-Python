def divisao(a,b):
    try: #tente
        resultado = a/b
        print(resultado)

    except ZeroDivisionError: #excessão
        print('Erro: Impossível dividir um valor por zero!')
    except TypeError as e:
        print(f'Erro: o tipo da dado informado está incorreto. \n Detalhes: {e}')
    else:
        print('Sem exceções!')
#divisao(10,2)
# divisao(10,0)
divisao(10,'womakerscode')