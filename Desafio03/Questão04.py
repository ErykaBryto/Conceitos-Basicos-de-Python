'''Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.'''

# Cria um dicionário para os contatos
contatos = {
    "Maria": "99999-1234",
    "João": "99999-5678",
    "Ana": "99999-8765",
    "Pedro": "99999-4321"
}

# Pede ao usuário para digitar o nome do contato que deseja procurar
nome_procurado = input("Digite o nome do contato que deseja procurar: ")

# Verifica se o contato existe no dicionário e exibe o telefone
if nome_procurado in contatos:
    print(f"O telefone de {nome_procurado} é {contatos[nome_procurado]}.")
else:
    print(f"Contato {nome_procurado} não encontrado.")
