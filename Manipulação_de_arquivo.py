def multiplicacao():
    mult = 10*2
    file = 'arquivo.txt'

    # Abertura de arquivo

    # Abertura para escrita
    arquivo_escrito = open(file,"w")
    arquivo_escrito.write(f'O resultado da multiplicação é:{mult}')
    arquivo_escrito.close() # fechando o arquivo

    # Leitura
    # open somente para leitura
    arquivo_leitura = open(file, "r") 
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()

    #print()

multiplicacao() #chamada da função